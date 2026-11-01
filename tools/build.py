"""Writes index.html, install.html and faq.html next to this folder's parent. Run: python3 tools/build.py"""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
VER = "2.0.0"
REL = "https://github.com/rNetGit/ShotReel-app/releases"
SETUP = f"{REL}/download/v{VER}/ShotReel-Setup-{VER}.exe"
PORT = f"{REL}/download/v{VER}/ShotReel-Portable-{VER}.exe"
SUMS = f"{REL}/download/v{VER}/SHA256SUMS.txt"
MAIL = "rnetphone1@gmail.com"

def head(title, desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/logo/icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/style.css">
<script src="assets/site.js"></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

def header(cur):
    def a(href, label, key):
        c = ' aria-current="page"' if cur == key else ''
        return f'<a href="{href}"{c}>{label}</a>'
    return f'''
<header class="top">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="assets/logo/icon.svg" alt=""> ShotReel <span>for Windows</span></a>
    <nav class="nav" aria-label="Main">
      {a("index.html","Home","home")}
      {a("index.html#how","How it works","how")}
      {a("install.html","Get ShotReel","install").replace('<a ','<a class="nav-cta" ',1)}
      {a("faq.html","FAQ","faq")}
      <button class="theme-btn" type="button" aria-label="Dark theme" aria-pressed="false">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
      </button>
    </nav>
  </div>
</header>

<main id="main">
'''

FOOT = f'''
</main>

<footer>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <a class="brand" href="index.html"><img src="assets/logo/icon.svg" alt=""> ShotReel <span>for Windows</span></a>
        <p style="margin:12px 0 0;max-width:28em">Turns screenshots and clicks into narrated training videos, captions and PDF step guides. Free, and it works offline.</p>
      </div>
      <div>
        <h4>Product</h4>
        <ul><li><a href="index.html#what">What it does</a></li><li><a href="index.html#how">How it works</a></li><li><a href="install.html">Download</a></li></ul>
      </div>
      <div>
        <h4>Help</h4>
        <ul><li><a href="faq.html">FAQ</a></li><li><a href="faq.html#contact">Contact</a></li><li><a href="https://github.com/rNetGit/ShotReel-app/issues" rel="noopener">Report a bug</a></li><li><a href="https://github.com/rNetGit/ShotReel-app/blob/main/EULA.txt" rel="noopener">Licence (EULA)</a></li><li><a href="https://github.com/rNetGit/ShotReel-app/blob/main/THIRD-PARTY-NOTICES.md" rel="noopener">Third-party notices</a></li></ul>
      </div>
    </div>
    <div class="fine">
      <div>Illustrations on this site are drawings of how ShotReel works, not screenshots of a customer's screens.</div>
      <div>Product names belong to their owners. ShotReel is a separate project from Mitra Home.</div>
    </div>
  </div>
</footer>
</body>
</html>
'''

def ico(path):
    return f'<span class="ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{path}</svg></span>'

# ---------- index ----------
mock = '''<div class="browser"><div class="chrome"><i></i><i></i><i></i></div>
  <div class="mock" role="img" aria-label="Illustration of the ShotReel editor: a list of steps on the left, the current step with a highlight box and a narration line on the right, and three outputs: MP4 video, captions and a PDF guide.">
    <div class="mock-steps">
      <b>Steps</b>
      <span class="on"><i>1</i> Open the admin portal</span>
      <span><i>2</i> Click Users</span>
      <span><i>3</i> Choose Add user</span>
      <span><i>4</i> Fill in the form</span>
      <span><i>5</i> Press Save</span>
    </div>
    <div class="mock-main">
      <div class="mock-shot"><div class="mock-box"></div><u></u><u></u><u></u></div>
      <div class="mock-say"><b>Narration</b> First, sign in to the admin portal with your work account.</div>
      <div class="mock-out"><span>MP4</span><span>SRT / VTT</span><span>PDF guide</span></div>
    </div>
  </div></div>'''

index = head("ShotReel for Windows", "ShotReel is a free Windows app that turns screenshots and clicks into narrated training videos, captions and PDF step guides. It works offline, with no account.") + header("home") + f'''
<div class="hero">
  <div class="wrap">
    <div>
      <a class="pre" href="install.html"><b>{VER}</b> First public release, code-signed</a>
      <h1>Training videos from your clicks.</h1>
      <p class="lead">ShotReel turns screenshots and clicks into a narrated video, captions and a printable step guide. It runs on your own Windows PC, with no account and no cloud service.</p>
      <div class="btns">
        <a class="btn btn-accent" href="install.html">Get ShotReel <span class="arr" aria-hidden="true">&rarr;</span></a>
        <a class="btn btn-outline" href="index.html#how">See how it works</a>
      </div>
      <p class="small muted" style="margin-top:12px">Download now ({VER}): <a href="{SETUP}" rel="noopener">Installer</a> &middot; <a href="{PORT}" rel="noopener">Portable</a> &middot; Windows 10 and 11, 64-bit</p>
      <ul class="facts">
        <li>Free, no account</li>
        <li>No watermark, no time limit</li>
        <li>Voice and rendering run on your PC</li>
      </ul>
    </div>
    <div class="stage">{mock}</div>
  </div>
</div>

<section id="how" class="alt">
  <div class="wrap">
    <div class="section-head center">
      <div class="eyebrow">How it works</div>
      <h2>Three steps from clicks to video</h2>
      <p class="muted">Record or import, write what each step says, then export. Nothing leaves the computer on the way.</p>
    </div>
    <div class="flow">
      <div class="step"><span class="num">1</span><h3>Capture</h3><p class="muted" style="margin:0">Click through a web app and every click becomes a step with its box already placed. Or click through a Windows desktop app and the control you clicked is named for you.</p></div>
      <div class="arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12h16M14 6l6 6-6 6"/></svg></div>
      <div class="step pc"><span class="num">2</span><h3>Narrate</h3><p class="muted" style="margin:0">Type the words for each step, and a built-in offline English voice reads them. Or export the script, edit it with any AI or writer, and import it back.</p></div>
      <div class="arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12h16M14 6l6 6-6 6"/></svg></div>
      <div class="step"><span class="num">3</span><h3>Export</h3><p class="muted" style="margin:0">Get an MP4 at 720p or 1080p, captions as <code>.srt</code> and <code>.vtt</code>, and a step-guide PDF to print or attach to a ticket.</p></div>
    </div>
    <p class="small muted" style="margin-top:16px">Prefer screenshots? Import them, or short screen clips, instead of capturing.</p>
  </div>
</section>

<section id="what">
  <div class="wrap">
    <div class="section-head center">
      <div class="eyebrow">What it does</div>
      <h2>Everything a how-to needs, in one app</h2>
    </div>

    <div class="feature">
      <div>
        <div class="eyebrow">Capture</div>
        <h2>Every click becomes a step.</h2>
        <p>Record a web app or a Windows desktop app and ShotReel builds the step list for you, each with a screenshot and the highlight in the right place.</p>
        <ul class="ticks">
          <li>Web apps: a step per click, box already placed</li>
          <li>Windows desktop apps: the clicked control is named for you</li>
          <li>Or import screenshots and short screen clips you already have</li>
        </ul>
      </div>
      <div class="shot"><div class="illus" role="img" aria-label="Illustration: a cursor clicking a button, with a numbered step appearing beside it."><div class="illus-btn">Save</div><div class="illus-cursor"></div><div class="illus-badge">3</div></div></div>
    </div>

    <div class="feature flip">
      <div>
        <div class="eyebrow">Annotate</div>
        <h2>Point at the thing that matters, hide the thing that does not.</h2>
        <p>Add boxes, arrows, spotlights, numbered badges and text notes, then zoom in on the part of the screen you are explaining. Blur or redact anything sensitive before it is rendered.</p>
        <ul class="ticks">
          <li>Boxes, arrows, spotlights, badges and text notes</li>
          <li>Zoom to a region of the screen</li>
          <li>Blur or redaction for customer or internal data</li>
        </ul>
      </div>
      <div class="shot"><div class="illus" role="img" aria-label="Illustration: a form with one field highlighted by a box and another field blurred out."><div class="illus-row"><i></i><s class="hl"></s></div><div class="illus-row"><i></i><s class="blur"></s></div><div class="illus-row"><i></i><s></s></div></div></div>
    </div>

    <div class="feature">
      <div>
        <div class="eyebrow">Narrate</div>
        <h2>A voice, without a microphone or a cloud.</h2>
        <p>Built-in English voices run on your PC. If you would rather have a person or an AI write the words, export the script, edit it anywhere and import it back.</p>
        <ul class="ticks">
          <li>Offline voices, nothing sent to a speech service</li>
          <li>Export the script, edit it, import it back</li>
          <li>Captions in <code>.srt</code> and <code>.vtt</code></li>
        </ul>
      </div>
      <div class="shot"><div class="illus" role="img" aria-label="Illustration: a sound wave beside a line of caption text."><div class="illus-wave"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div><div class="illus-cap">First, sign in to the admin portal.</div></div></div>
    </div>

    <div class="feature flip">
      <div>
        <div class="eyebrow">Export and reuse</div>
        <h2>A video, captions and a guide, from the same steps.</h2>
        <p>One project gives you an MP4 (720p or 1080p, no watermark), caption files and a printable PDF. When you change one step, only that part is rendered again, and a whole project shares as a single <code>.shotreel</code> file.</p>
        <ul class="ticks">
          <li>MP4, captions and PDF step guide</li>
          <li>Unchanged parts are not re-rendered</li>
          <li>Share a project as one <code>.shotreel</code> file</li>
        </ul>
      </div>
      <div class="shot"><div class="illus" role="img" aria-label="Illustration: one project file on the left with three arrows to a video, a captions file and a PDF."><div class="illus-out"><b>.shotreel</b><span>MP4</span><span>SRT / VTT</span><span>PDF</span></div></div></div>
    </div>
  </div>
</section>

<section class="alt" id="teams">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Why teams use it</div>
      <h2>Built for people who cannot send screens to the cloud</h2>
    </div>
    <div class="table-wrap"><table>
      <thead><tr><th>Concern</th><th>Answer</th></tr></thead>
      <tbody>
        <tr><td>Our screens contain customer or internal data</td><td>Everything is processed on the computer. Redaction tools are built in.</td></tr>
        <tr><td>We cannot use cloud tools</td><td>There is no cloud service to approve, and no account or sign-in.</td></tr>
        <tr><td>We do not want another subscription</td><td>The free version has no time limit, watermark or project cap.</td></tr>
        <tr><td>We need to review it</td><td>The installer is code-signed, and the licence and third-party notices ship with the download.</td></tr>
      </tbody>
    </table></div>
  </div>
</section>

<section id="free">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Price</div>
      <h2>Free, and staying free</h2>
      <p class="muted">The core features in this version stay free. Later versions may add paid extras for teams, such as 4K output, batch rendering and branding. Nothing you have today will be taken away.</p>
    </div>
    <div class="cols">
      <div><span class="num">Free</span><h3>Use it at work</h3><p>Free to use, including at work. You may not resell or redistribute ShotReel.</p></div>
      <div><span class="num">Needs</span><h3>A normal Windows PC</h3><p>Windows 10 or 11 (64-bit), about 2 GB of free disk space and 8 GB of RAM recommended. Rendering uses the CPU, so a longer video takes longer.</p></div>
      <div><span class="num">Size</span><h3>About 650 MB installed</h3><p>The voice model, renderer and video tools are bundled, so it works with no further downloads.</p></div>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="cta">
      <div>
        <h2>Make your first video today.</h2>
        <p>Download, install for your own user (no admin rights), and record a short how-to. Tell us what is missing and it decides what gets built next.</p>
      </div>
      <div class="btns">
        <a class="btn btn-dark" href="install.html">Get ShotReel <span class="arr" aria-hidden="true">&rarr;</span></a>
        <a class="btn btn-line" href="faq.html">Read the FAQ</a>
      </div>
    </div>
  </div>
</section>
''' + FOOT

# ---------- install ----------
install = head("Get ShotReel", "Download ShotReel for Windows 10 and 11: the installer or the portable version, how to check the download, and what to do about the SmartScreen notice.") + header("install") + f'''
<section>
  <div class="wrap" style="max-width:820px">
    <div class="section-head">
      <div class="eyebrow">Download</div>
      <h1>Get ShotReel {VER}</h1>
      <p class="muted">For Windows 10 and 11, 64-bit. Both files are code-signed (publisher: Rajesh Katukojwala).</p>
    </div>

    <div class="choices" style="margin-bottom:12px">
      <a class="choice" href="{SETUP}" rel="noopener">
        <span class="ctag beta">Recommended</span>
        {ico('<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>')}
        <strong>Installer</strong>
        <span>A normal install, per user, no admin rights needed. About 586 MB to download.</span>
      </a>
      <a class="choice" href="{PORT}" rel="noopener">
        {ico('<path d="M4 17v3h16v-3M12 4v12M7 11l5 5 5-5"/>')}
        <strong>Portable</strong>
        <span>Run it without installing, for example on a borrowed PC. About 535 MB to download.</span>
      </a>
    </div>
    <p class="small muted">All versions and notes are on the <a href="{REL}/latest" rel="noopener">release page</a>.</p>

    <h2 style="margin-top:40px">Install</h2>
    <ol class="steps">
      <li><h3>Download</h3><p>Choose the installer, or the portable file if you cannot install software. About 650 MB is used once it is installed, because the voice model, renderer and video tools are bundled.</p></li>
      <li><h3>Run it</h3><p>Double-click the file. If Windows shows a blue <strong>SmartScreen</strong> notice, that is normal for a new publisher's first downloads: choose <strong>More info</strong>, then <strong>Run anyway</strong>. The signature below lets you check who published it.</p></li>
      <li><h3>Make a video</h3><p>Start a project, capture a web or desktop app or import screenshots, write the steps, and choose Export. You get an MP4, captions and a PDF guide.</p></li>
    </ol>

    <h2 style="margin-top:8px" id="verify">Check the download</h2>
    <p class="muted">Not required, but quick, and worth doing on a work PC.</p>
    <details open>
      <summary>Check the file's SHA-256</summary>
      <p>Download <a href="{SUMS}" rel="noopener"><code>SHA256SUMS.txt</code></a> from the release, then in PowerShell (from the folder with the file):</p>
      <p><code>Get-FileHash .\\ShotReel-Setup-{VER}.exe -Algorithm SHA256</code></p>
      <p>The hash must match the line for that file in <code>SHA256SUMS.txt</code>.</p>
    </details>
    <details>
      <summary>Check the signature</summary>
      <p>Right-click the file, choose <strong>Properties</strong>, open the <strong>Digital Signatures</strong> tab and select the signature, then <strong>Details</strong>. It should say the signature is OK and name the publisher Rajesh Katukojwala. If the tab is missing, the file is not signed: do not run it.</p>
    </details>
    <details>
      <summary>Read the licence first</summary>
      <p>The <a href="https://github.com/rNetGit/ShotReel-app/blob/main/EULA.txt" rel="noopener">EULA</a> and the <a href="https://github.com/rNetGit/ShotReel-app/blob/main/THIRD-PARTY-NOTICES.md" rel="noopener">third-party notices</a> are in the repository and in the download.</p>
    </details>

    <h2 style="margin-top:32px" id="trouble">If something goes wrong</h2>
    <details>
      <summary>Windows blocked it or my antivirus complains</summary>
      <p>Check the SHA-256 and the signature above. If both are right, the file is the one we published. If your IT team scans downloads, send them the release page and the licence.</p>
    </details>
    <details>
      <summary>A long video renders slowly</summary>
      <p>Rendering uses the CPU, so length and 1080p both add time. Unchanged parts are not re-rendered, so the second export of a project is much quicker than the first.</p>
    </details>
    <details>
      <summary>Still stuck</summary>
      <p>Open an <a href="https://github.com/rNetGit/ShotReel-app/issues" rel="noopener">issue</a> or email <a href="mailto:{MAIL}">{MAIL}</a>. Say your Windows version and what you clicked last.</p>
    </details>
  </div>
</section>
''' + FOOT

# ---------- faq ----------
def qa(q, a, op=False):
    return f'    <details{" open" if op else ""}>\n      <summary>{q}</summary>\n      <p>{a}</p>\n    </details>\n'

faq = head("ShotReel FAQ", "Plain answers about ShotReel: cost, privacy, Windows support, voices, exports and how to get help.") + header("faq") + f'''
<section>
  <div class="wrap" style="max-width:820px">
    <div class="section-head">
      <div class="eyebrow">Questions</div>
      <h1>Plain answers</h1>
    </div>

    <h2>Cost</h2>
''' + qa("Is ShotReel free?", "Yes. The free version has no time limit, no watermark and no project cap, and it is free to use at work.", True) \
  + qa("Will it stay free?", "The core features in this version stay free, and nothing you have today will be taken away. Later versions may add paid extras for teams, such as 4K output, batch rendering and branding.") \
  + qa("Can I resell it or hand out copies?", f'No. You may use it, including at work, but you may not resell or redistribute it. Point people to this site instead. The full terms are in the <a href="https://github.com/rNetGit/ShotReel-app/blob/main/EULA.txt" rel="noopener">EULA</a>.') \
  + '''
    <h2 style="margin-top:32px">Privacy</h2>
''' + qa("Does it upload my screens?", "No. Capture, voice and rendering all run on your PC. There is no account, no cloud service and no API key to set up.") \
  + qa("Our screens contain customer data. Is that a problem?", "Everything is processed on the computer, and ShotReel has blur and redaction tools so sensitive parts are hidden before the video is rendered. Check the finished video before you share it, as you would any recording.") \
  + qa("Can the voice use an AI service?", "The built-in voices are offline. If you want AI-written narration, you can export the script, edit it with any AI or writer on your own terms, and import it back.") \
  + '''
    <h2 style="margin-top:32px">Using it</h2>
''' + qa("Which computers does it run on?", "Windows 10 and 11, 64-bit. Plan for about 2 GB of free disk space and 8 GB of RAM. There is no Mac or Linux version yet.") \
  + qa("What does it capture?", "Web apps, where every click becomes a step with the box already placed, and Windows desktop apps, where the clicked control is named for you. You can also import screenshots and short screen clips.") \
  + qa("What do I get out?", "An MP4 at 720p or 1080p with no watermark, captions as <code>.srt</code> and <code>.vtt</code>, and a step-guide PDF.") \
  + qa("Which languages can it speak?", "The built-in offline voices are English. Captions and the PDF contain whatever text you write.") \
  + qa("Why is it so large?", "About 650 MB installed, because the voice model, renderer and video tools are bundled. That is what lets it work offline.") \
  + qa("Can I share a project?", "Yes. A project saves as a single <code>.shotreel</code> file you can send to a colleague who has ShotReel.") \
  + f'''
    <h2 style="margin-top:32px" id="contact">Contact</h2>
''' + qa("How do I report a bug or ask for a feature?", f'Open an <a href="https://github.com/rNetGit/ShotReel-app/issues" rel="noopener">issue</a> or email <a href="mailto:{MAIL}">{MAIL}</a>. Teams that want a paid tier or a pilot: tell us what you need, it decides what gets built next.') + f'''
    <p style="margin-top:32px"><a href="install.html">Get ShotReel &rarr;</a></p>
  </div>
</section>
''' + FOOT

for name, html in (("index.html", index), ("install.html", install), ("faq.html", faq)):
    (ROOT / name).write_text(html, encoding="utf-8")
    print(name, len(html))
