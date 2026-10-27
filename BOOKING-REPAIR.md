# Verified consultation delivery

The old booking form saved requests only in the visitor's localStorage, showed a received confirmation, emitted patient details to the advertising data layer, then attempted to open WhatsApp. It did not deliver a callback request to a server.

The repaired form posts to `/api/consultation`. This Vercel function forwards the request to the clinic's existing Apps Script deployment used by the consultation landing pages. No new email/CRM provider is introduced. The optional `BOOKING_APPS_SCRIPT_URL` server environment variable can point to an updated deployment on `script.google.com`; never place credentials in HTML.

Success requires a 2xx upstream response containing JSON with `ok: true`, `success: true`, `status: "success"` or `result: "success"`, without an error. An echoed request ID, when supplied, must match. HTML error pages, opaque responses, timeouts, invalid JSON and negative acknowledgements do not count as success. The API returns only an acknowledgement and the request ID to the browser.

The existing service's POST acknowledgement and saved test row were verified on 27 October 2026 before production release. Its GET endpoint currently reports `Script function not found: doGet`; that does not establish whether POST writes work. Confirm that the upstream response means the clinic's lead was saved, not merely that the script ran. For reliable retries after an ambiguous timeout, the Apps Script handler should deduplicate `lead_id` before inserting a row. This repository does not contain that handler and cannot establish its current behaviour.

The browser keeps one request ID across an unchanged retry, prevents simultaneous submissions, and emits the verified Google Ads primary action `AW-18375933203/91coCMuK5uscEJP6qbpE` only after acknowledgement. No name, phone, condition or preferred time enters this event. GTM is removed only from the booking page so another form-submit tag cannot independently count that page's form. Other pages retain their existing tag setup. Advertising user-data and personalisation signals are denied before tags load on the booking page.

The optional concern selector is not required to request a callback. Successful requests remain on the page; WhatsApp is an explicit contact action. Failed/unconfirmed requests retain the form and show call/WhatsApp alternatives. Previews neither forward leads nor count conversions; the server also refuses Vercel preview deployments. Existing browser-only records are not deleted.

## Validation

Run `node --test tests/booking.test.cjs`. Tests mock the upstream service and make no live submissions. They cover acknowledgements, failures, validation, preview isolation, limited response data, phone normalisation, retry IDs and conversion timing. The actual form was also checked in a localhost browser preview.

Vercel deploys the committed `public` directory; its build command currently only creates that directory. Both the booking template and committed page are updated. `build.py` keeps the booking-specific GTM exclusion when the page is regenerated. The new function has a 60-second maximum duration and a 30-second upstream timeout; the browser waits 35 seconds.

## Release verification

1. Confirm the existing Apps Script POST acknowledgement and lead-save semantics using an explicitly authorised test request.
2. Review a Vercel preview; it deliberately cannot send to the live clinic sheet.
3. Release the reviewed branch through the project's normal production deployment.
4. Submit one clearly labelled, authorised production test without ad-click identifiers. Confirm it reaches the clinic's lead register and that an unavailable service shows an honest failure state.
5. Keep page views, phone-button clicks and WhatsApp clicks separate from received form requests. Reconcile unique enquiries and attended appointments with the clinic's register.

After local validation, the user authorised one labelled test request. The service returned HTTP 200 with `result: "success"`, and the clinic confirmed that the test was received. This backend-only check sent no WhatsApp message and fired no browser advertising event. No payment was performed. No further live enquiry was submitted.

References: [Vercel Node.js functions](https://vercel.com/docs/functions/runtimes/node-js), [Google customer-data policy](https://support.google.com/adspolicy/answer/7475709), [Google consent controls](https://developers.google.com/tag-platform/security/guides/consent).
