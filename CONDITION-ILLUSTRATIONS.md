# Homepage condition illustrations

The homepage's 20 chronic-condition cards use original graphical medical illustrations rather than the previous small monochrome line icons. The images use natural ivory anatomy, coral and rose tissues, amber highlights and slate-blue accents on warm neutral backgrounds.

These are conceptual representations of condition topics, not patient scans, diagnostic diagrams or treatment outcomes. They contain no treatment claims or before-and-after comparisons.

## Sources and rendering

- Edit the card markup in `templates/index.html`; the deployed static copy is `public/index.html`.
- Homepage-only responsive styles are in `css/condition-illustrations.css` and `public/css/condition-illustrations.css`.
- All final images are in `images/condition-illustrations/` and `public/images/condition-illustrations/`.
- Exact final prompts are recorded in `data/condition-illustration-prompts.json`. All assets were generated with the built-in image-generation tool; resizing and WebP encoding followed generation.
- Site images are 600 × 400 pixels, with explicit HTML dimensions, descriptive alternative text, lazy loading and asynchronous decoding.

The conditions-directory page retains its existing compact icons. Homepage labels, destinations and surrounding content are preserved. The normal `build.py` asset copy and homepage render include the new source files on subsequent builds.

## Verification

The template and static page each contain exactly 20 illustrated cards. Card destinations match the previous version in the same order. Checks confirmed no changes outside this section and its stylesheet reference, and `git diff --check` passed. Desktop and mobile browser previews were inspected; the 375-pixel mobile layout has two columns and no horizontal overflow.
