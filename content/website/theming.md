Title: Adventures in Themes
Date: 11:54 AM 3/18/2015
Category: Projects
Tags: Website, CSS, Jinja


Theming a new website is very much an tiresome labor of sifting through hundreds of identical black-on-white bootstrap templates. Despite my initial hopes, in the end it came down to nitpicky manual editing to produce something that would pass muster.

For example - Email me at <span class="icon-envelope"></span> [web@tofof.com](mailto:web@tofof.com)

Even that simple glyph took quite a bit of fiddling with CSS files. Putting it into the navigation bar required even more tweaking, now with Jinja thrown into the mix. This was, of course, before I realized that I was reverse-engineering basically the exact same CSS that already present in bootstrap. At least I gained a familiarity in the process, but it's a familiarity I was hoping to avoid.

That's on top of a host of problems with the theme as it stood. I was cleaning up everything from the obvious (h1 being smaller than h2) to the fiddly (roman numbering of footnotes). Missing titles were added, icons were inlined, passive voice was passive-aggressively used, and slowly but surely this website adopted my aesthetic.


