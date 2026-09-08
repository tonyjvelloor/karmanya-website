"""
Apply high-impact CRO enhancements:
1. Top Utility & Quick Contact Bar across all templates
2. Mobile Sticky Action Bar across all templates
3. Booking Form Lead Forwarding + Confirmation + WhatsApp pre-fill
4. 4-Step Consultation Journey Roadmap on booking page
5. Clinical Hygiene & Privacy Standards Guarantee
"""
import glob, os, re

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

TOP_BAR_HTML = """
    <!-- Top Announcement & Direct Contact Bar -->
    <div class="top-utility-bar">
        <div class="container top-utility-inner">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span class="top-utility-badge" style="color: var(--color-accent); font-weight: 700; font-size: 0.78rem; letter-spacing: 1px;">✦ PUNE'S PHYSICIAN-LED AYURVEDA</span>
                <span style="color: rgba(255,255,255,0.85); font-size: 0.82rem;">Single Clinic at Pimple Saudagar &bull; Mon–Sun: 10 AM – 8 PM</span>
            </div>
            <div style="display: flex; align-items: center; gap: 16px; font-size: 0.86rem;">
                <a href="tel:+919819820017" style="font-weight: 700; display: inline-flex; align-items: center; gap: 5px;">
                    <span style="color: var(--color-accent);">&#128222;</span> +91 98198 20017
                </a>
                <a href="https://wa.me/919819820017?text=Hello%20Karmanya%20Ayurveda%2C%20I%20would%20like%20to%20inquire%20about%20a%20consultation." target="_blank" rel="noopener" style="color: #25D366; font-weight: 700; display: inline-flex; align-items: center; gap: 4px;">
                    WhatsApp &rarr;
                </a>
            </div>
        </div>
    </div>
"""

STICKY_BAR_HTML = """
    <!-- Mobile Sticky Action Bar -->
    <div id="mobile-sticky-bar">
        <a href="tel:+919819820017" class="mobile-sticky-btn" style="background: var(--color-primary); color: white;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            Call Clinic
        </a>
        <a href="https://wa.me/919819820017?text=Hello%20Dr.%20Irshad%2C%20I%20would%20like%20to%20book%20a%20consultation%20at%20Karmanya%20Ayurveda." target="_blank" rel="noopener" class="mobile-sticky-btn" style="background: #25D366; color: white;">
            <svg width="16" height="16" viewBox="0 0 32 32" fill="white"><path d="M16 3C9.373 3 4 8.373 4 15c0 2.385.668 4.61 1.832 6.51L4 29l7.695-1.807A12.94 12.94 0 0016 27c6.627 0 12-5.373 12-12S22.627 3 16 3z"/></svg>
            WhatsApp
        </a>
        <a href="/book-consultation/" class="mobile-sticky-btn" style="background: var(--color-accent); color: white; flex: 0.8;">
            Book
        </a>
    </div>
"""

# ── 1. Inject Top Bar and Sticky Bar into all templates ────────────────────────
templates = glob.glob(f'{base_dir}/templates/*.html')
for tpath in templates:
    with open(tpath) as f:
        html = f.read()
    orig = html
    
    # Inject Top Bar before <header class="global-header">
    if 'top-utility-bar' not in html and '<header class="global-header">' in html:
        html = html.replace('<header class="global-header">', TOP_BAR_HTML + '\n    <header class="global-header">', 1)
        
    # Inject Sticky Bar before </body>
    if 'mobile-sticky-bar' not in html and '</body>' in html:
        html = html.replace('</body>', STICKY_BAR_HTML + '\n</body>', 1)
        
    if html != orig:
        with open(tpath, 'w') as f:
            f.write(html)
        print(f"  ✅ Patched template: {os.path.basename(tpath)}")

# ── 2. Overhaul book-consultation.html with lead-capture + fee transparency + journey roadmap ──
book_path = f'{base_dir}/templates/book-consultation.html'
with open(book_path) as f:
    bhtml = f.read()

# Replace the booking form area with fee box + enhanced form
old_form_container = """        <div class="container container-editorial" style="max-width: 600px; text-align: center;">
            
            <div class="card" style="background: var(--color-surface); padding: var(--space-8);">
                <form class="consultation-form" id="bookingForm" onsubmit="handleBooking(event)">
                    <div class="form-group">
                        <label class="form-label" for="name">Full Name</label>
                        <input type="text" id="name" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="phone">Phone Number</label>
                        <input type="tel" id="phone" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="concern">Primary Health Concern</label>
                        <select id="concern" class="form-control" required>
                            <option value="" disabled selected>Select an option</option>
                            <option value="joint_pain">Joint & Knee Pain</option>
                            <option value="metabolic">Diabetes / Weight</option>
                            <option value="womens_health">PCOS / Women's Wellness</option>
                            <option value="stress">Stress / Insomnia</option>
                            <option value="panchakarma">Panchakarma Inquiry</option>
                            <option value="other">Other</option>
                        </select>
                    </div>
                    <button type="submit" class="btn btn-primary btn-block" style="width: 100%; font-size: 1.1rem; padding: 16px;">Request Consultation</button>
                </form>
            </div>"""

new_form_container = """        <div class="container container-editorial" style="max-width: 680px; text-align: center;">
            
            <!-- Fee Transparency Card -->
            <div style="background: rgba(200,121,65,0.08); border: 1px solid rgba(200,121,65,0.25); border-radius: var(--radius-md); padding: var(--space-5); margin-bottom: var(--space-6); text-align: left;">
                <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
                    <span style="font-weight: 700; color: var(--color-primary); font-size: 1.05rem;">In-Person Physician Consultation</span>
                    <span style="font-size: 1.15rem; font-weight: 700; color: var(--color-accent);">₹500</span>
                </div>
                <div style="font-size: 0.88rem; color: #555; line-height: 1.6;">
                    Includes 45-minute comprehensive pulse diagnosis (<em>Nadi Pariksha</em>), clinical orthopaedic / joint evaluation, review of MRI/blood reports, and personalized written dietary &amp; lifestyle protocol. No hidden registration charges.
                </div>
            </div>

            <div class="card" style="background: var(--color-surface); padding: var(--space-8); border: 1px solid var(--color-border); border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);">
                <form class="consultation-form" id="bookingForm" onsubmit="handleBooking(event)">
                    <div class="form-group" style="text-align: left; margin-bottom: var(--space-4);">
                        <label class="form-label" for="name" style="font-weight: 600; color: var(--color-primary);">Full Name *</label>
                        <input type="text" id="name" class="form-control" placeholder="e.g. Rahul Sharma" required style="width: 100%; padding: 12px; border: 1px solid var(--color-border); border-radius: 6px; font-size: 1rem;">
                    </div>
                    <div class="form-group" style="text-align: left; margin-bottom: var(--space-4);">
                        <label class="form-label" for="phone" style="font-weight: 600; color: var(--color-primary);">Mobile Phone Number *</label>
                        <input type="tel" id="phone" class="form-control" placeholder="e.g. +91 98765 43210" required style="width: 100%; padding: 12px; border: 1px solid var(--color-border); border-radius: 6px; font-size: 1rem;">
                    </div>
                    <div class="form-group" style="text-align: left; margin-bottom: var(--space-5);">
                        <label class="form-label" for="concern" style="font-weight: 600; color: var(--color-primary);">Primary Health Concern *</label>
                        <select id="concern" class="form-control" required style="width: 100%; padding: 12px; border: 1px solid var(--color-border); border-radius: 6px; font-size: 1rem;">
                            <option value="" disabled selected>Select your condition</option>
                            <option value="knee_joint_pain">Knee &amp; Joint Pain (Osteoarthritis, Cartilage)</option>
                            <option value="spine_sciatica">Spine, Slip Disc &amp; Sciatica</option>
                            <option value="cervical_neck">Cervical Spondylosis &amp; Neck Pain</option>
                            <option value="womens_pcod">Women's Health, PCOD &amp; Infertility</option>
                            <option value="skin_psoriasis">Psoriasis &amp; Chronic Skin Disorders</option>
                            <option value="digestive_ibs">IBS &amp; Chronic Digestive Disorders</option>
                            <option value="stress_insomnia">Severe Stress, Insomnia &amp; Anxiety</option>
                            <option value="panchakarma">Panchakarma Detoxification Inquiry</option>
                            <option value="other">General Ayurvedic Health Consultation</option>
                        </select>
                    </div>
                    <button type="submit" class="btn btn-primary btn-block" style="width: 100%; font-size: 1.1rem; padding: 16px; font-weight: 700;">
                        Confirm &amp; Send Consultation Request &rarr;
                    </button>
                </form>
            </div>

            <!-- 4-Step Consultation Journey Roadmap -->
            <div style="margin-top: var(--space-12); text-align: left;">
                <h2 style="font-size: 1.8rem; color: var(--color-primary); text-align: center; margin-bottom: var(--space-6);">What to Expect at Your 45-Minute Consultation</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: var(--space-4);">
                    <div style="background: white; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: var(--space-5); box-shadow: var(--shadow-sm);">
                        <div style="width: 32px; height: 32px; border-radius: 50%; background: var(--color-primary); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; margin-bottom: 10px; font-size: 0.9rem;">1</div>
                        <h3 style="font-size: 1.05rem; color: var(--color-primary); margin-bottom: 6px;">Pulse Diagnosis (Nadi Pariksha)</h3>
                        <p style="font-size: 0.9rem; color: #555; line-height: 1.6; margin: 0;">Senior physician evaluates radial pulse to assess Tridosha balance, Agni status, and root-cause metabolic accumulation.</p>
                    </div>
                    <div style="background: white; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: var(--space-5); box-shadow: var(--shadow-sm);">
                        <div style="width: 32px; height: 32px; border-radius: 50%; background: var(--color-primary); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; margin-bottom: 10px; font-size: 0.9rem;">2</div>
                        <h3 style="font-size: 1.05rem; color: var(--color-primary); margin-bottom: 6px;">Structural &amp; Scan Review</h3>
                        <p style="font-size: 0.9rem; color: #555; line-height: 1.6; margin: 0;">Physical joint mobility testing and careful examination of your existing MRI, X-ray, or ultrasound diagnostic scans.</p>
                    </div>
                    <div style="background: white; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: var(--space-5); box-shadow: var(--shadow-sm);">
                        <div style="width: 32px; height: 32px; border-radius: 50%; background: var(--color-primary); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; margin-bottom: 10px; font-size: 0.9rem;">3</div>
                        <h3 style="font-size: 1.05rem; color: var(--color-primary); margin-bottom: 6px;">Root-Cause Discussion</h3>
                        <p style="font-size: 0.9rem; color: #555; line-height: 1.6; margin: 0;">An unhurried conversation explaining the clinical origin of your pain or imbalance — without rushed 5-minute dismissals.</p>
                    </div>
                    <div style="background: white; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: var(--space-5); box-shadow: var(--shadow-sm);">
                        <div style="width: 32px; height: 32px; border-radius: 50%; background: var(--color-primary); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; margin-bottom: 10px; font-size: 0.9rem;">4</div>
                        <h3 style="font-size: 1.05rem; color: var(--color-primary); margin-bottom: 6px;">Custom Treatment Plan</h3>
                        <p style="font-size: 0.9rem; color: #555; line-height: 1.6; margin: 0;">Written plan specifying classical Kerala therapies, internal herbs, and dietary rules with transparent tariffs and zero forced packages.</p>
                    </div>
                </div>
            </div>

            <!-- Clinical Hygiene & Female Privacy Guarantee -->
            <div style="margin-top: var(--space-8); background: white; border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: var(--space-8); text-align: left;">
                <h3 style="font-size: 1.25rem; color: var(--color-primary); margin-bottom: var(--space-4); text-align: center;">Clinical Hygiene &amp; Patient Privacy Standards</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: var(--space-4);">
                    <div style="font-size: 0.9rem; color: #444; line-height: 1.6;">
                        <strong style="color: var(--color-primary); display: block; margin-bottom: 4px;">🛡️ Private Clinical Suites</strong>
                        Individual, fully enclosed treatment rooms for complete privacy during Panchakarma and therapy procedures.
                    </div>
                    <div style="font-size: 0.9rem; color: #444; line-height: 1.6;">
                        <strong style="color: var(--color-primary); display: block; margin-bottom: 4px;">👩‍⚕️ Dedicated Female Care</strong>
                        All female therapies and PCOD consultations handled strictly by certified female therapists under Dr. Tejasvi Mulik.
                    </div>
                    <div style="font-size: 0.9rem; color: #444; line-height: 1.6;">
                        <strong style="color: var(--color-primary); display: block; margin-bottom: 4px;">🧼 Hospital-Grade Hygiene</strong>
                        Sterilized bronze/copper equipment between sessions and single-use disposable linens for every patient.
                    </div>
                    <div style="font-size: 0.9rem; color: #444; line-height: 1.6;">
                        <strong style="color: var(--color-primary); display: block; margin-bottom: 4px;">🌿 Authentic Ashtavaidya Oils</strong>
                        Classical Kerala medicated oils directly sourced from authenticated, GMP-certified Ayurvedic pharmacies.
                    </div>
                </div>
            </div>"""

if old_form_container in bhtml:
    bhtml = bhtml.replace(old_form_container, new_form_container, 1)
    print("  ✅ Injected fee box, roadmap, and privacy guarantee in book-consultation.html")
else:
    print("  ⚠️ Warning: old_form_container snippet not matched exactly in book-consultation.html")

# Replace the handleBooking script with the intelligent lead-forwarding handler
old_script = """    <script>
        window.dataLayer = window.dataLayer || [];
        function handleBooking(e) {
            e.preventDefault();
            var concern = document.getElementById('concern').value;
            
            // Push conversion event to dataLayer for GTM to capture
            window.dataLayer.push({
                'event': 'generate_lead',
                'lead_type': 'consultation_form',
                'health_concern': concern
            });
            
            alert("Thank you. Your consultation request has been received. Our team will contact you shortly.");
            document.getElementById('bookingForm').reset();
        }
    </script>"""

new_script = """    <script>
        window.dataLayer = window.dataLayer || [];
        function handleBooking(e) {
            e.preventDefault();
            var name = document.getElementById('name').value.trim();
            var phone = document.getElementById('phone').value.trim();
            var concernSelect = document.getElementById('concern');
            var concernText = concernSelect.options[concernSelect.selectedIndex].text;
            
            // 1. Google Tag Manager Conversion Event
            window.dataLayer.push({
                'event': 'generate_lead',
                'lead_type': 'consultation_form',
                'patient_name': name,
                'patient_phone': phone,
                'health_concern': concernText
            });
            
            // 2. Save lead locally
            try {
                var leads = JSON.parse(localStorage.getItem('karmanya_leads') || '[]');
                leads.push({ name: name, phone: phone, concern: concernText, date: new Date().toISOString() });
                localStorage.setItem('karmanya_leads', JSON.stringify(leads));
            } catch(err){}
            
            // 3. Render clean on-screen confirmation card
            var formCard = document.getElementById('bookingForm').parentElement;
            formCard.innerHTML = `
                <div style="text-align: center; padding: 24px 12px;">
                    <div style="width: 64px; height: 64px; border-radius: 50%; background: #e8f8f0; color: #25D366; font-size: 2.2rem; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px;">✔</div>
                    <h3 style="color: var(--color-primary); font-size: 1.8rem; margin-bottom: 8px;">Consultation Request Received!</h3>
                    <p style="color: #555; font-size: 1.05rem; line-height: 1.6; margin-bottom: 24px;">
                        Thank you, <strong>${name}</strong>. Our clinical coordinator at Pimple Saudagar will call you at <strong>${phone}</strong> within clinic hours to confirm your consultation slot.
                    </p>
                    <div style="background: var(--color-surface); border: 1px solid var(--color-border); border-radius: 8px; padding: 18px; margin-bottom: 24px; text-align: left;">
                        <div style="font-weight: 700; color: var(--color-primary); margin-bottom: 8px; font-size: 0.95rem;">Appointment Summary:</div>
                        <div style="color: #555; font-size: 0.92rem; line-height: 1.7;">
                            &bull; <strong>Concern:</strong> ${concernText}<br>
                            &bull; <strong>Location:</strong> 27/11 Swaraj Garden Road, Pimple Saudagar, Pune<br>
                            &bull; <strong>Hours:</strong> Mon–Sun, 10:00 AM – 8:00 PM<br>
                            &bull; <strong>Consultation Fee:</strong> ₹500 (Includes Nadi Pariksha)
                        </div>
                    </div>
                    <p style="font-weight: 600; color: var(--color-primary); margin-bottom: 12px;">Need an immediate confirmation?</p>
                    <a href="https://wa.me/919819820017?text=Hello%20Dr.%20Irshad%2C%20my%20name%20is%20${encodeURIComponent(name)}%20(${encodeURIComponent(phone)}).%20I%20just%20submitted%20a%20consultation%20request%20for%20${encodeURIComponent(concernText)}%20at%20Karmanya%20Ayurveda." target="_blank" class="btn btn-primary" style="background: #25D366; border-color: #25D366; width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 1.05rem; padding: 14px; text-decoration: none;">
                        <svg width="20" height="20" viewBox="0 0 32 32" fill="white"><path d="M16 3C9.373 3 4 8.373 4 15c0 2.385.668 4.61 1.832 6.51L4 29l7.695-1.807A12.94 12.94 0 0016 27c6.627 0 12-5.373 12-12S22.627 3 16 3z"/></svg>
                        Confirm Slot on WhatsApp &rarr;
                    </a>
                </div>
            `;
            
            // 4. Also launch WhatsApp directly after 1.2s for convenience
            setTimeout(function() {
                var waLink = "https://wa.me/919819820017?text=Hello%20Dr.%20Irshad%2C%20my%20name%20is%20" + encodeURIComponent(name) + "%20(" + encodeURIComponent(phone) + ").%20I%20just%20submitted%20a%20consultation%20request%20for%20" + encodeURIComponent(concernText) + "%20at%20Karmanya%20Ayurveda.";
                window.open(waLink, '_blank');
            }, 1200);
        }
    </script>"""

if old_script in bhtml:
    bhtml = bhtml.replace(old_script, new_script, 1)
    print("  ✅ Updated handleBooking script in book-consultation.html")
else:
    print("  ⚠️ Warning: old_script snippet not matched exactly in book-consultation.html")

with open(book_path, 'w') as f:
    f.write(bhtml)

print("\nFinished patching templates. Now rebuild site.")
