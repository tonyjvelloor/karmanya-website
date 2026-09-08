base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

with open(f'{base_dir}/templates/index.html', 'r') as f:
    html = f.read()

# Replace the entire section from line 156 to 238 (Kerala + Approach sections)
old_section = html[html.find('<section class="section-padding section-kerala"'):html.find('<!-- Senior Physician Panel')]

new_section = '''<section class="section-padding section-kerala" style="background-color: var(--color-bg); position: relative;">
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0.03; background-image: radial-gradient(var(--color-primary) 1px, transparent 1px); background-size: 20px 20px; z-index: 0;"></div>
        <div class="container container-editorial" style="position: relative; z-index: 1; text-align: center;" data-aos="fade-up">
            <div style="margin-bottom: var(--space-4);">
                <span style="display: inline-block; background: rgba(200, 121, 65, 0.15); border: 1px solid var(--color-accent); color: var(--color-accent); padding: 6px 18px; border-radius: 30px; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px;">✦ CERTIFIED BEST AYURVEDIC CENTRE IN INDIA ✦</span>
            </div>
            <span style="display: block; font-size: 0.85rem; font-weight: 600; color: var(--color-accent); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: var(--space-4);">Our Clinical Specialties</span>
            <h2 style="font-size: 3.5rem; margin-bottom: var(--space-6);">Conditions we treat at Karmanya.</h2>
            <p style="font-size: 1.25rem; margin-bottom: var(--space-12); color: #555; max-width: 680px; margin-left: auto; margin-right: auto;">We are a physician-led clinical treatment centre. Therapies are prescribed based on diagnosis — not chosen from a spa menu. Every patient protocol is unique.</p>
            <div class="grid-2" style="text-align: left; margin-bottom: var(--space-12);">
                <div class="card luxury-card" style="border-left: 3px solid var(--color-accent); position: relative;">
                    <span style="font-size: 0.75rem; font-weight: 700; color: var(--color-accent); text-transform: uppercase; letter-spacing: 1.5px; display: block; margin-bottom: var(--space-2);">Clinical Treatment</span>
                    <h4 style="color: var(--color-primary); font-size: 1.5rem; font-family: var(--font-heading); text-transform: none; letter-spacing: 0; margin-bottom: var(--space-2);">Knee &amp; Joint Pain</h4>
                    <p style="font-size: 0.95rem; margin-bottom: var(--space-4); color: #555;">Non-surgical management of osteoarthritis and cartilage degeneration through Janu Basti and targeted herbal protocols. Avoid knee replacement.</p>
                    <a href="/conditions/knee-joint-pain/" style="font-size: 0.9rem; color: var(--color-accent); font-weight: 600;">Read Treatment Protocol &rarr;</a>
                </div>
                <div class="card luxury-card" style="border-left: 3px solid var(--color-accent); position: relative;">
                    <span style="font-size: 0.75rem; font-weight: 700; color: var(--color-accent); text-transform: uppercase; letter-spacing: 1.5px; display: block; margin-bottom: var(--space-2);">Clinical Treatment</span>
                    <h4 style="color: var(--color-primary); font-size: 1.5rem; font-family: var(--font-heading); text-transform: none; letter-spacing: 0; margin-bottom: var(--space-2);">Spine, Sciatica &amp; Slip Disc</h4>
                    <p style="font-size: 0.95rem; margin-bottom: var(--space-4); color: #555;">Non-invasive nerve decompression through Kati Basti, disc nourishment therapies, and medicated Basti enema for L4-L5 disc conditions.</p>
                    <a href="/conditions/spine-sciatica-back-pain/" style="font-size: 0.9rem; color: var(--color-accent); font-weight: 600;">Read Treatment Protocol &rarr;</a>
                </div>
                <div class="card luxury-card" style="border-left: 3px solid var(--color-accent); position: relative;">
                    <span style="font-size: 0.75rem; font-weight: 700; color: var(--color-accent); text-transform: uppercase; letter-spacing: 1.5px; display: block; margin-bottom: var(--space-2);">Clinical Treatment</span>
                    <h4 style="color: var(--color-primary); font-size: 1.5rem; font-family: var(--font-heading); text-transform: none; letter-spacing: 0; margin-bottom: var(--space-2);">PCOD &amp; Hormonal Disorders</h4>
                    <p style="font-size: 0.95rem; margin-bottom: var(--space-4); color: #555;">Cycle regularisation, insulin resistance correction, and fertility support through classical Panchakarma and Rasayana protocols.</p>
                    <a href="/conditions/womens-health-pcod-hormonal/" style="font-size: 0.9rem; color: var(--color-accent); font-weight: 600;">Read Treatment Protocol &rarr;</a>
                </div>
                <div class="card luxury-card" style="border-left: 3px solid var(--color-accent); position: relative;">
                    <span style="font-size: 0.75rem; font-weight: 700; color: var(--color-accent); text-transform: uppercase; letter-spacing: 1.5px; display: block; margin-bottom: var(--space-2);">Clinical Treatment</span>
                    <h4 style="color: var(--color-primary); font-size: 1.5rem; font-family: var(--font-heading); text-transform: none; letter-spacing: 0; margin-bottom: var(--space-2);">Psoriasis &amp; Skin Disorders</h4>
                    <p style="font-size: 0.95rem; margin-bottom: var(--space-4); color: #555;">Internal blood purification (Raktashodhana) and Takradhara for chronic psoriasis and eczema — addressing the root metabolic cause, not just symptoms.</p>
                    <a href="/conditions/skin-disorders-psoriasis/" style="font-size: 0.9rem; color: var(--color-accent); font-weight: 600;">Read Treatment Protocol &rarr;</a>
                </div>
            </div>
            <a href="/conditions/" class="btn btn-secondary" style="border-color: var(--color-accent); color: var(--color-primary); font-size: 1rem; padding: 12px 30px;">View All Conditions We Treat &rarr;</a>
        </div>
    </section>

    <!-- Not a Spa — Differentiator Section -->
    <section class="section-padding" style="background: var(--color-primary); color: var(--color-white);">
        <div class="container container-editorial" style="text-align: center;">
            <span style="display: block; font-size: 0.85rem; font-weight: 600; color: var(--color-accent); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: var(--space-4);">What Makes Us Different</span>
            <h2 style="font-size: clamp(2rem, 4vw, 3rem); color: var(--color-white); margin-bottom: var(--space-4);">We treat conditions. We don\'t sell packages.</h2>
            <p style="font-size: 1.15rem; color: rgba(255,255,255,0.75); max-width: 680px; margin: 0 auto var(--space-12);">Many Ayurvedic centres offer spa packages and relaxation sessions. Karmanya is structured differently — as a physician-managed clinical treatment centre where every session is medically directed.</p>
            <div class="grid-2" style="text-align: left; gap: var(--space-8);">
                <div style="border-top: 2px solid var(--color-accent); padding-top: var(--space-6);">
                    <h3 style="color: var(--color-accent); font-size: 1.3rem; margin-bottom: var(--space-3);">What we are NOT</h3>
                    <ul style="list-style: none; padding: 0; color: rgba(255,255,255,0.7); line-height: 2.4; font-size: 1rem;">
                        <li>&#10007; &nbsp; A day spa or wellness lounge</li>
                        <li>&#10007; &nbsp; A walk-in package centre</li>
                        <li>&#10007; &nbsp; Generic relaxation massage therapy</li>
                        <li>&#10007; &nbsp; A place where you pick your own treatment</li>
                        <li>&#10007; &nbsp; Short-cut, quick-fix Ayurveda</li>
                    </ul>
                </div>
                <div style="border-top: 2px solid var(--color-accent); padding-top: var(--space-6);">
                    <h3 style="color: var(--color-accent); font-size: 1.3rem; margin-bottom: var(--space-3);">What we ARE</h3>
                    <ul style="list-style: none; padding: 0; color: rgba(255,255,255,0.85); line-height: 2.4; font-size: 1rem;">
                        <li>&#10004; &nbsp; A physician-led clinical treatment centre</li>
                        <li>&#10004; &nbsp; Formal diagnosis before every protocol</li>
                        <li>&#10004; &nbsp; Condition-specific, structured treatment plans</li>
                        <li>&#10004; &nbsp; Physician oversight during every therapy session</li>
                        <li>&#10004; &nbsp; Follow-up, diet protocols &amp; herbal medicines</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- The Clinical Process -->
    <section class="section-padding" style="background: var(--color-surface); border-top: 1px solid var(--color-border); border-bottom: 1px solid var(--color-border);">
        <div class="container">
            <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: var(--space-8); flex-wrap: wrap; gap: var(--space-6);">
                <div style="max-width: 600px;">
                    <span style="display: block; font-size: 0.85rem; font-weight: 600; color: var(--color-accent); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: var(--space-2);">Our Clinical Process</span>
                    <h2 style="font-size: 3rem; margin-bottom: 0;">How your treatment works.</h2>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(12, 1fr); align-items: center; gap: 0; position: relative;">
                <div style="grid-column: 1 / 9; position: relative; border-radius: var(--radius-leaf); overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.1); z-index: 1;">
                    <img src="/images/doctor-consult.jpg" alt="Ayurvedic Doctor Consultation at Karmanya" style="width: 100%; height: 600px; object-fit: cover; display: block; filter: sepia(0.15) contrast(1.1);">
                </div>
                <div style="grid-column: 7 / 13; background: var(--color-bg); padding: var(--space-8); border-radius: var(--radius-md); box-shadow: 0 10px 50px rgba(14,35,21,0.08); position: relative; z-index: 2; margin-top: 40px; border-left: 3px solid var(--color-accent);" data-aos="fade-left" data-aos-delay="200">
                    <div class="method-grid" style="display: flex; flex-direction: column; gap: var(--space-6);">
                        <div style="display: flex; gap: var(--space-4);">
                            <span style="color: var(--color-accent); font-family: var(--font-heading); font-size: 2.5rem; line-height: 1; font-style: italic;">01</span>
                            <div>
                                <h3 style="font-size: 1.5rem; margin-bottom: var(--space-1); font-family: var(--font-heading);">Clinical Diagnosis</h3>
                                <p style="font-size: 1rem; margin-bottom: 0; color: #555;">Nadi Pariksha (pulse diagnosis), medical history, and Dosha assessment by a qualified physician to identify the root cause — not just the symptoms.</p>
                            </div>
                        </div>
                        <div style="display: flex; gap: var(--space-4);">
                            <span style="color: var(--color-accent); font-family: var(--font-heading); font-size: 2.5rem; line-height: 1; font-style: italic;">02</span>
                            <div>
                                <h3 style="font-size: 1.5rem; margin-bottom: var(--space-1); font-family: var(--font-heading);">Prescribed Treatment Plan</h3>
                                <p style="font-size: 1rem; margin-bottom: 0; color: #555;">The physician prescribes a structured protocol — specific therapies, sessions, internal herbal medicines, and dietary restrictions — tailored to your condition.</p>
                            </div>
                        </div>
                        <div style="display: flex; gap: var(--space-4);">
                            <span style="color: var(--color-accent); font-family: var(--font-heading); font-size: 2.5rem; line-height: 1; font-style: italic;">03</span>
                            <div>
                                <h3 style="font-size: 1.5rem; margin-bottom: var(--space-1); font-family: var(--font-heading);">Physician-Monitored Therapy</h3>
                                <p style="font-size: 1rem; margin-bottom: 0; color: #555;">Every therapy session is conducted under physician oversight. Progress is monitored, and protocols are adjusted based on your body\'s clinical response.</p>
                            </div>
                        </div>
                        <div style="display: flex; gap: var(--space-4);">
                            <span style="color: var(--color-accent); font-family: var(--font-heading); font-size: 2.5rem; line-height: 1; font-style: italic;">04</span>
                            <div>
                                <h3 style="font-size: 1.5rem; margin-bottom: var(--space-1); font-family: var(--font-heading);">Follow-up &amp; Long-Term Cure</h3>
                                <p style="font-size: 1rem; margin-bottom: 0; color: #555;">Post-therapy diet protocol, herbal medicine regimen, and review consultations to sustain the cure and prevent relapse of your condition.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

'''

html = html.replace(old_section, new_section)

with open(f'{base_dir}/templates/index.html', 'w') as f:
    f.write(html)

print("Homepage repositioned successfully.")
