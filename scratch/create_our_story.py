import os
import glob

base_dir = '/Users/tonyvelloor/.gemini/antigravity/scratch/karmanya-website'

with open(f"{base_dir}/templates/doctors.html", "r") as f:
    doctors_html = f.read()

header_part = doctors_html.split('</header>')[0] + '</header>'

# Find where the footer begins (search for Unified Clinic Location & Contact Bar, or the first script after section-padding)
# The content is between </header> and <!-- Floating WhatsApp Widget --> or <!-- Unified Clinic Location...
footer_split = doctors_html.split('<!-- Floating WhatsApp Widget -->')
if len(footer_split) < 2:
    # try looking for <script>
    footer_split = doctors_html.split('<script>')
    footer_part = '<script>' + footer_split[1]
else:
    footer_part = '<!-- Floating WhatsApp Widget -->' + footer_split[1]

# Inject the "Our Story" content
content = """
    <div class="hero-doctors" style="padding: 6rem 0 3rem; background: var(--color-cream); text-align: center;">
        <div class="container container-editorial">
            <h1 style="font-size: clamp(2rem, 4vw, 3.5rem); margin-bottom: 1rem; color: var(--color-primary);">Why We Started Karmanya Ayurveda</h1>
            <p style="font-size: 1.2rem; color: #555; max-width: 800px; margin: 0 auto;">The Story of Two Friends and a Shared Belief</p>
        </div>
    </div>

    <section class="section-padding">
        <div class="container container-editorial" style="max-width: 800px; margin: 0 auto; font-size: 1.1rem; line-height: 1.8; color: #333;">
            <p style="font-size: 1.3rem; font-weight: 600; color: var(--color-accent); text-align: center; margin-bottom: 3rem;">Two friends. Two different journeys. One belief in the power of authentic Ayurveda.</p>
            
            <p>There are some decisions that begin with a business plan.</p>
            <p>And then there are decisions that begin with a belief.</p>
            <p><strong>Karmanya Ayurveda began with a belief.</strong></p>
            <p>A belief that Ayurveda is far more than what people often see on the surface.</p>
            <p>It is not simply a massage.</p>
            <p>It is not simply a collection of herbal medicines.</p>
            <p>It is not a trend that has suddenly become popular.</p>
            <p><strong>Ayurveda is a profound body of knowledge &mdash; one that has been understood, practiced and passed down for generations.</strong></p>
            <p>We wanted more people to experience that depth.</p>
            <p>And that is where our journey began.</p>

            <hr style="margin: 3rem 0; border: 0; border-top: 1px solid var(--color-border);">

            <h2 style="color: var(--color-primary); margin-bottom: 1.5rem;">Before Karmanya, There Was a Friendship</h2>
            <p>Our story started years before Karmanya had a name.</p>
            <p>We first met as students during our graduation in Ayurveda.</p>
            <p><strong>Dr. Anandu</strong> was born in Kerala and brought up in Pune.</p>
            <p><strong>Dr. Aditya</strong> came from Mumbai.</p>
            <p>Different cities. Different experiences. Different stories.</p>
            <p>But as we spent more time together studying Ayurveda, we discovered that we shared something much more important &mdash; a genuine curiosity about the science we had chosen to learn.</p>
            <p>What started as a friendship slowly became a journey of learning together.</p>
            <p>We discussed what we studied.</p>
            <p>We questioned what we were taught.</p>
            <p>We observed.</p>
            <p>We learned from our teachers.</p>
            <p>And with every year, Ayurveda became less like a subject we were studying and more like a way of understanding health itself.</p>

            <hr style="margin: 3rem 0; border: 0; border-top: 1px solid var(--color-border);">

            <h2 style="color: var(--color-primary); margin-bottom: 1.5rem;">The More We Learned, The More We Realised</h2>
            <p>One of the most fascinating things about Ayurveda is that it doesn't begin by asking only,</p>
            <p><strong>&ldquo;What disease do you have?&rdquo;</strong></p>
            <p>It asks us to understand the person.</p>
            <ul style="list-style-type: disc; margin-left: 2rem; margin-bottom: 1.5rem; color: #555;">
                <li>Their constitution.</li>
                <li>Their lifestyle.</li>
                <li>Their habits.</li>
                <li>Their environment.</li>
                <li>Their digestion.</li>
                <li>Their daily routine.</li>
                <li>Their mental and physical wellbeing.</li>
                <li>And the factors that may have contributed to an imbalance.</li>
            </ul>
            <p>The deeper we went into Ayurveda, the more we realised that this way of thinking was incredibly relevant to the world we live in today.</p>
            <p>Because modern life has changed dramatically.</p>
            <p>Our food has changed. Our routines have changed. Our sleep has changed. Our work has changed. Our stress has changed.</p>
            <p>But our need to understand our health has not.</p>
            <p>That realisation stayed with us.</p>

            <hr style="margin: 3rem 0; border: 0; border-top: 1px solid var(--color-border);">

            <h2 style="color: var(--color-primary); margin-bottom: 1.5rem;">Why Pune?</h2>
            <p>For us, Pune wasn't simply a location on a map.</p>
            <p>It was personal.</p>
            <p>For Dr. Anandu, Pune was home.</p>
            <p>He was born in Kerala but grew up in this city. He understood both worlds &mdash; the cultural roots of Kerala and the rapidly evolving lifestyle of Pune.</p>
            <p>Dr. Aditya brought his own perspective from Mumbai &mdash; another city shaped by ambition, speed and modern urban life.</p>
            <p>And somewhere between these two experiences, we saw an opportunity.</p>
            <p>We saw a city where people were increasingly conscious about their health.</p>
            <p>People were searching for holistic approaches.</p>
            <p>People were rediscovering traditional knowledge.</p>
            <p>But we also felt that there was an opportunity to make <strong>authentic Ayurvedic knowledge more accessible, more understandable and more relevant to the people living here.</strong></p>
            <p>We didn't want to simply bring a name from Kerala to Pune.</p>
            <p><strong>We wanted to bring the knowledge behind it.</strong></p>

            <hr style="margin: 3rem 0; border: 0; border-top: 1px solid var(--color-border);">

            <h2 style="color: var(--color-primary); margin-bottom: 1.5rem;">We Didn't Want to Build Just Another Ayurveda Clinic</h2>
            <p>This became the most important question for us.</p>
            <p>If we were going to create something of our own, <strong>what should it stand for?</strong></p>
            <p>The answer was clear.</p>
            <p>We wanted to build a place where Ayurveda was approached with respect.</p>
            <p>Where a patient was not simply a symptom.</p>
            <p>Where treatment was not reduced to a package.</p>
            <p>Where traditional therapies were supported by proper understanding.</p>
            <p>Where every individual could be looked at as an individual.</p>
            <p>And where the authenticity of Ayurveda was reflected not only in the therapies we offered, but in the <strong>way we thought about healthcare.</strong></p>
            <p>That vision became Karmanya.</p>

            <hr style="margin: 3rem 0; border: 0; border-top: 1px solid var(--color-border);">

            <h2 style="color: var(--color-primary); margin-bottom: 1.5rem;">Why Kerala Ayurveda?</h2>
            <p>Kerala holds a special place in the history and practice of Ayurveda.</p>
            <p>For us, Kerala represents something deeper than a geographical identity.</p>
            <p>It represents <strong>heritage, knowledge and continuity.</strong></p>
            <p>Dr. Anandu's connection to Kerala made this particularly personal.</p>
            <p>But our intention was never to romanticise the past.</p>
            <p>We believe tradition becomes meaningful when it continues to serve people in the present.</p>
            <p>That is why our goal is not to recreate yesterday.</p>
            <p>It is to bring the principles and practices of authentic Ayurveda into the lives of people today.</p>
            <p><strong>Rooted in tradition. Relevant to modern life.</strong></p>
            <p>That is the balance we continue to pursue.</p>

            <hr style="margin: 3rem 0; border: 0; border-top: 1px solid var(--color-border);">

            <h2 style="color: var(--color-primary); margin-bottom: 1.5rem;">Karmanya Is Our Answer</h2>
            <p>Starting Karmanya was our way of turning that belief into something tangible.</p>
            <p>A place where people could come not merely to seek a treatment, but to understand their health from an Ayurvedic perspective.</p>
            <p>A place where consultation comes before assumptions.</p>
            <p>Where understanding comes before intervention.</p>
            <p>Where the individual matters.</p>
            <p>And where the wisdom of Ayurveda is treated with the seriousness it deserves.</p>
            <p>Our approach today continues to revolve around personalized Ayurvedic consultations and traditional therapies, including Panchakarma and Keraliya Chikitsa.</p>
            <p>But for us, these are not the destination.</p>
            <p>They are part of a larger philosophy.</p>
            <div style="background: var(--color-cream); padding: 2rem; border-left: 4px solid var(--color-accent); margin: 2rem 0;">
                <p style="margin:0; font-weight: 600; font-style: italic; color: var(--color-primary);">Understand the person.<br>Understand the imbalance.<br>Understand the journey.<br>Then begin the process of care.</p>
            </div>

            <hr style="margin: 3rem 0; border: 0; border-top: 1px solid var(--color-border);">

            <h2 style="color: var(--color-primary); margin-bottom: 1.5rem;">We Are Still Young. And That Is Okay.</h2>
            <p>We don't look at Karmanya as the finished version of our dream.</p>
            <p>It is the beginning.</p>
            <p>We are still learning.</p>
            <p>Still listening.</p>
            <p>Still meeting patients who teach us something new every day.</p>
            <p>Still discovering how ancient knowledge can be thoughtfully applied to modern lives.</p>
            <p>And perhaps that is one of the most beautiful parts of this journey.</p>
            <p>We didn't start Karmanya because we believed we had all the answers.</p>
            <p><strong>We started it because we believed the questions were worth asking.</strong></p>
            <ul style="list-style-type: disc; margin-left: 2rem; margin-bottom: 1.5rem; color: #555;">
                <li>What can Ayurveda mean to someone living with the pressures of modern life?</li>
                <li>How can traditional knowledge remain relevant without losing its authenticity?</li>
                <li>How can we make people understand Ayurveda beyond the stereotypes surrounding it?</li>
                <li>And how can we build a healthcare experience that people can genuinely trust?</li>
            </ul>
            <p>These questions continue to guide us.</p>

            <hr style="margin: 3rem 0; border: 0; border-top: 1px solid var(--color-border);">

            <h2 style="color: var(--color-primary); margin-bottom: 1.5rem;">From Two Friends to a Shared Mission</h2>
            <p>When we look back, Karmanya feels like a natural extension of the journey that began during our college years.</p>
            <p>Two young students became friends.</p>
            <p>Those friends became doctors.</p>
            <p>And those doctors eventually decided to build something together.</p>
            <p>Something rooted in what they had learned.</p>
            <p>Something influenced by where they came from.</p>
            <p>And something designed for the people and the city they call home.</p>
            <p><strong>Karmanya Ayurveda is our attempt to bring authentic Ayurveda closer to the people of Pune.</strong></p>
            <p>Not because Ayurveda needs to be reinvented.</p>
            <p>But because we believe it deserves to be <strong>understood.</strong></p>
            <p>Not because tradition belongs only in the past.</p>
            <p>But because the right knowledge can continue to shape the future.</p>

            <hr style="margin: 3rem 0; border: 0; border-top: 1px solid var(--color-border);">

            <h2 style="color: var(--color-primary); margin-bottom: 1.5rem;">And This Is Only the Beginning</h2>
            <p>Every patient who walks through our doors becomes part of this journey.</p>
            <p>Every consultation teaches us something.</p>
            <p>Every experience challenges us to become better.</p>
            <p>And every day gives us another opportunity to do what we set out to do in the first place:</p>
            <div style="background: var(--color-cream); padding: 2rem; border-left: 4px solid var(--color-accent); margin: 2rem 0;">
                <p style="margin:0; font-weight: 600; font-style: italic; color: var(--color-primary);">Preserve the authenticity.<br>Respect the knowledge.<br>Understand the individual.<br>And make Ayurveda meaningful for modern life.</p>
            </div>
            <p>Karmanya began with two friends and a shared belief.</p>
            <p>Today, that belief is becoming a larger mission.</p>
            <p>A mission to bring the depth of <strong>authentic Kerala Ayurveda to Pune.</strong></p>
            <p>And we believe this journey has only just begun.</p>

            <div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--color-border); text-align: center;">
                <p style="font-weight: 600; font-size: 1.2rem; color: var(--color-accent); margin-bottom: 1rem;">
                    With roots in Kerala.<br>With a home in Pune.<br>And with a vision for the future.
                </p>
                <p style="font-weight: 700; color: var(--color-primary); margin-bottom: 0;">&mdash; Dr. Anandu & Dr. Aditya</p>
                <p style="color: #666; font-size: 0.9rem;">Founders, Karmanya Ayurveda</p>
            </div>

            <div style="text-align: center; margin-top: 4rem;">
                <a href="/book-consultation/" class="btn btn-primary" style="padding: 12px 24px; font-size: 1.1rem;">Book a Consultation with Us</a>
            </div>
        </div>
    </section>
"""

full_html = header_part + content + '\n' + footer_part

with open(f"{base_dir}/templates/our-story.html", "w") as f:
    f.write(full_html)

# Add nav links
templates = glob.glob(f'{base_dir}/templates/*.html')
for t in templates:
    with open(t, 'r') as f:
        tmpl = f.read()
    
    if '<a href="/our-story/" class="nav-link">Our Story</a>' not in tmpl:
        tmpl = tmpl.replace('<a href="/doctors/" class="nav-link">Our Doctors</a>', 
                           '<a href="/our-story/" class="nav-link">Our Story</a>\n                <a href="/doctors/" class="nav-link">Our Doctors</a>')
        
        tmpl = tmpl.replace('<a href="/doctors/" class="mobile-nav-link">Our Doctors</a>',
                           '<a href="/our-story/" class="mobile-nav-link">Our Story</a>\n            <a href="/doctors/" class="mobile-nav-link">Our Doctors</a>')
                           
        with open(t, 'w') as f:
            f.write(tmpl)

print("Our Story template created and navigation links updated.")

# Also update build.py to build it!
with open(f"{base_dir}/build.py", "r") as f:
    build_script = f.read()

story_build_code = """
    # Render Our Story
    with open(os.path.join(base_dir, 'templates', 'our-story.html'), 'r') as f:
        story_template = f.read()
    out_dir = os.path.join(base_dir, 'public', 'our-story')
    os.makedirs(out_dir, exist_ok=True)
    site_data['seo_head_tags'] = '''<title>Founders’ Story | Authentic Kerala Ayurveda in Pune | Karmanya</title>
<meta name="description" content="Discover the story behind Karmanya Ayurveda, founded by Dr. Anandu and Dr. Aditya to bring authentic Kerala Ayurveda and traditional Ayurvedic knowledge to Pune.">
<meta property="og:title" content="Why We Started Karmanya Ayurveda">
<meta property="og:description" content="The story of two friends and a shared belief in authentic Kerala Ayurveda.">
<meta property="og:url" content="https://karmanyaayurveda.com/our-story/">'''
    with open(os.path.join(out_dir, 'index.html'), 'w') as f:
        f.write(render_template(story_template, site_data))
        
    # Render Homepage
"""
if "Render Our Story" not in build_script:
    build_script = build_script.replace("# 6. Render Homepage", story_build_code.strip() + "\n\n    # 6. Render Homepage")
    with open(f"{base_dir}/build.py", "w") as f:
        f.write(build_script)
    print("build.py updated.")

