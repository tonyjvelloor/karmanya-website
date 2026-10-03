import re

with open('templates/knee-pain-care-program.html', 'r') as f:
    html = f.read()

tracking_scripts = """
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-NP2DTL98');</script>
    <!-- End Google Tag Manager -->

    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=AW-18375933203"></script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-QWH0NSNLVE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'AW-18375933203');
      gtag('config', 'G-QWH0NSNLVE');
    </script>
    
    <!-- Meta Pixel Code -->
    <script>
    !function(f,b,e,v,n,t,s)
    {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};
    if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
    n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];
    s.parentNode.insertBefore(t,s)}(window, document,'script',
    'https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', '2147354382501419');
    fbq('track', 'PageView');
    </script>
    <noscript><img height="1" width="1" style="display:none"
    src="https://www.facebook.com/tr?id=2147354382501419&ev=PageView&noscript=1"
    /></noscript>
    <!-- End Meta Pixel Code -->
</head>
"""

html = html.replace('</head>', tracking_scripts)

# Now inject the event listener before </body>
event_listener = """
    <!-- Conversion Tracking Scripts -->
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        var buttons = document.querySelectorAll('.btn-primary, .btn-whatsapp');
        buttons.forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                // Determine if WhatsApp or Consult
                var actionType = this.classList.contains('btn-whatsapp') ? 'WhatsApp_Click' : 'Consult_Click';
                
                // Fire GAds Conversion (Lead)
                gtag('event', 'conversion', {
                    'send_to': 'AW-18375933203/91coCMuK5uscEJP6qbpE'
                });
                
                // Fire GA4 Event
                gtag('event', 'generate_lead', {
                    'event_category': 'Engagement',
                    'event_label': actionType,
                    'value': 1
                });
                
                // Push to GTM DataLayer
                window.dataLayer = window.dataLayer || [];
                window.dataLayer.push({
                    'event': 'generate_lead',
                    'lead_type': actionType
                });
                
                // Fire Meta Pixel Lead Event
                if (typeof fbq !== 'undefined') {
                    fbq('track', 'Lead');
                }
            });
        });
    });
    </script>
</body>
"""

html = html.replace('</body>', event_listener)

with open('templates/knee-pain-care-program.html', 'w') as f:
    f.write(html)
