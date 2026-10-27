(function () {
  'use strict';
  var pending = false, completed = false, requestKey = '', leadId = '';
  var production = /^(www\.)?karmanyaayurveda\.com$/.test(location.hostname);
  var form = document.getElementById('bookingForm');
  var status = document.getElementById('bookingStatus');
  var button = form.querySelector('button[type="submit"]');
  window.handleBooking = async function (event) {
    event.preventDefault();
    if (pending || completed) return;
    var name = document.getElementById('name').value.trim();
    var phone = window.KarmanyaBooking.cleanPhone(document.getElementById('phone').value);
    var phoneInput = document.getElementById('phone');
    phoneInput.setCustomValidity(/^[6-9]\d{9}$/.test(phone) ? '' : 'Enter a valid 10-digit Indian mobile number.');
    phoneInput.oninput = function () { phoneInput.setCustomValidity(''); };
    if (!form.reportValidity() || name.length < 2) return;
    if (!production) {
      status.textContent = 'Preview only: your request has not been sent. Please use the published clinic website.';
      status.hidden = false;
      return;
    }
    var concern = document.getElementById('concern').value || 'other';
    var timeslot = document.getElementById('timeslot').value;
    var key = JSON.stringify([name, phone, concern, timeslot]);
    if (key !== requestKey) { requestKey = key; leadId = window.KarmanyaBooking.newLeadId(); }
    pending = true;
    button.disabled = true;
    button.textContent = 'Sending your request…';
    status.hidden = true;
    try {
      await window.KarmanyaBooking.send({ name: name, phone: phone, concern: concern, timeslot: timeslot,
        lead_id: leadId, website: document.getElementById('bookingWebsite').value,
        page: location.origin + location.pathname });
    } catch (_) {
      status.setAttribute('role', 'alert');
      status.textContent = 'We could not confirm receipt of your request. Please call +91 98198 20017 or use the WhatsApp button to arrange your visit.';
      status.hidden = false;
      button.disabled = false;
      button.textContent = 'Retry appointment request';
      pending = false;
      return;
    }
    completed = true;
    pending = false;
    form.hidden = true;
    status.setAttribute('role', 'status');
    status.textContent = 'Your consultation request has been received. The clinic will contact you during opening hours to confirm availability. Your appointment is confirmed only when the clinic agrees a time with you.';
    status.hidden = false;
    status.focus();
    // Only an acknowledged request fires the verified primary action. Never pass patient data.
    try {
      if (typeof window.gtag === 'function') window.gtag('event', 'conversion', {
        send_to: 'AW-18375933203/91coCMuK5uscEJP6qbpE', transaction_id: leadId,
      });
    } catch (_) { /* Analytics must never affect a received booking. */ }
  };
})();
