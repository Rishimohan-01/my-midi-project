import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

hero_snippet = '''
<!-- hero section -->

    <section class="hero-section">

        <div id="heroCarousel" class="carousel slide carousel-fade" data-bs-ride="carousel">

            <div class="carousel-inner">

                <!-- Slide 1 -->
                <div class="carousel-item active">
                    <img src="IMGPATH/Header Banner/1.jpg" class="d-block w-100" alt="Slide 1">
                    <div class="overlay"></div>
                </div>

                <!-- Slide 2 -->
                <div class="carousel-item">
                    <img src="IMGPATH/Header Banner/2.jpg" class="d-block w-100" alt="Slide 2">
                    <div class="overlay"></div>
                </div>

                <!-- Slide 3 -->
                <div class="carousel-item">
                    <img src="IMGPATH/Header Banner/3.jpg" class="d-block w-100" alt="Slide 3">
                    <div class="overlay"></div>
                </div>

                <!-- Slide 4 -->
                <div class="carousel-item">
                    <img src="IMGPATH/Header Banner/4.jpg" class="d-block w-100" alt="Slide 3">
                    <div class="overlay"></div>
                </div>

                <!-- Slide 5 -->
                <div class="carousel-item">
                    <img src="IMGPATH/Header Banner/5.png" class="d-block w-100" alt="Slide 3">
                    <div class="overlay"></div>
                </div>

                <!-- Slide 6 -->
                <div class="carousel-item">
                    <img src="IMGPATH/Header Banner/6.png" class="d-block w-100" alt="Slide 3">
                    <div class="overlay"></div>
                </div>

                <!-- Slide 7 -->
                <div class="carousel-item">
                    <img src="IMGPATH/Header Banner/7.png" class="d-block w-100" alt="Slide 3">
                    <div class="overlay"></div>
                </div>

            </div>

        </div>

        <!-- Hero Content -->
        <div class="hero-content text-center text-white">
            <h1 class="display-4 fw-bold">Welcome to <span style="color: #84b7ff;">Maharashtra Industries Development
                    Institute</span></h1>
            <p class="lead">Building modern, responsive and powerful web solutions
                with clean UI and seamless performance.</p>
            <a href="#" class="btn hero-btn-1 btn-lg mt-3 me-3 px-4">Get Started</a>
            <a href="#" class="btn hero-btn-2 btn-outline-light btn-lg px-4">
                Learn More
            </a>
        </div>

    </section>
'''


def adjust_img_path(snippet, relprefix):
    return snippet.replace('IMGPATH', relprefix + 'images')


def process_file(path: Path):
    text = path.read_text(encoding='utf-8')
    orig = text

    # Remove Header Banner section if present (from comment to the following comment Navbar)
    text = re.sub(r'<!--\s*Header Banner\s*-->.*?<!--\s*Navbar\s*-->', '<!-- Navbar -->', text, flags=re.S)

    # Remove any <div class="header-banner"> blocks (fallback)
    text = re.sub(r'<div\s+class="header-banner">.*?</div>\s*</div>\s*', '', text, flags=re.S)

    # Remove blue-banner container blocks
    text = re.sub(r'<!--\s*=====?\s*Blue Banner\s*=====?\s*-->.*?<div\s+class="container\s+blue-banner">.*?</div>\s*</div>\s*', '', text, flags=re.S)
    text = re.sub(r'<div\s+class="container\s+blue-banner">.*?</div>\s*', '', text, flags=re.S)

    # Insert hero snippet after first closing </nav> if not contact page
    if path.name.lower() != 'contact.html':
        if '</nav>' in text:
            # compute relative prefix for images
            relprefix = ''
            # if file is inside pages/..., images need '../../' prefix
            try:
                rel = path.relative_to(ROOT)
            except Exception:
                rel = path
            if len(rel.parts) >= 2 and rel.parts[0] == 'pages':
                relprefix = '../../'
            elif len(rel.parts) >= 1 and rel.parts[0] == 'wow-slider':
                relprefix = '../../'
            else:
                relprefix = ''
            snippet = adjust_img_path(hero_snippet, relprefix)
            # avoid adding duplicate hero if already present
            if 'class="hero-section"' not in text:
                text = text.replace('</nav>', '</nav>\n\n' + snippet, 1)

    if text != orig:
        path.write_text(text, encoding='utf-8')
        print(f'Updated: {path}')
    else:
        print(f'No changes: {path}')


if __name__ == '__main__':
    html_files = list(ROOT.rglob('*.html'))
    for f in html_files:
        process_file(f)
    print('Done')
