Title: LLM hot takes
Date: 2025-5-14
Category: Personal
Tags: LLM
Author: Julz

To us developers, LLMs are that quintessential 'threat and opportunity' that we've all heard about. Sometimes I wonder if 
two commentators are sharing the same baseline experience Some bloggers say 'vibe coding is the goat'; others say: 'bah, it barely works'. What's going on?

Needless to say the truth is probably somewhere in between and nuanced. Hopefully this is some of that nuance!

* I've found 'LLM as super-autocomplete' really interesting for learning new frameworks and languages. With a bit of foundational knowledge, I can just make vague gestures towards
the direction I want and the 'LLM as super-autocomplete' kicks in. Does it help me learn, be productive and get results? Not sure. Feels like a win, but maintainability and best practices are 
  still my responsibility and (as a beginner to the new language) still an unknown - as a novice with the skill.  

* Skill atrophy: so LLM feel like a huge skills buff - but what about skill atrophy? I think it's too early to tell but I can imagine development reflexes and muscle-memory 
  dissapating. 
  It could mean that we defer most coding tasks to the LLM and work on a higher level, leaving us to do all architecture and design, & almost no implementation.
* I worry about what this means to the industry in general: Junior devs won't need to learn fundamentals. You get what you reward and if we reward relying on LLMs, then juniors preferentially 
  defer to LLMs
  and 
  not on their own knowledge.
* Junior's won't be reading code so frequently either: a vital learning stage; just vibe coding new slop.  
* I do think it's likely to hollow out the mid-tier of the developer workforce. Given the rate of change in the industry there's a surprising number of devs that are not very adaptable to change: 
  give me a Jira ticket. Not comfortable with any ambiguity. 'My end of the boat isn't sinking' mentality. This approach is very vulnerable to being replaced by an LLM, sadly.

* How are LLM on the 'day-to-day'? It's quite a peculiar change in a 'think-do-check' work cycle, and takes some getting used to. There's definitely a process of acclimatization and change of habits. 
* I find the interruptions to my usual habits mean getting into a 'flow state' of work has changed; bit harder. Still pondering this one tbh.
* And 
  what's a good metaphor for 
  working with 
  them? Something like:
  * 'An excitable indefatigable junior': They have lots of energy and have crammed a lot of knowledge but don't know how to apply it. We're pair programming partners, but I have to keep it as unequal 
    as possible.
  * 'A Genie': You give them commands and magically they do what you ask. With unintended consequences (that are often extremely unfortunate), so keep them on a short leash!
  * 'As excitable interns': Different to being a 'junior' as they just don't care about any consequences. They fulfil the task and they're on to the next thing.
  * A 'sycophantic fabulist': they'll flatter you and tell you pleasant lies. And cheat if they have to. Tests don't pass? No problem, they'll just delete them.

* This change in habits can apply to non-developer roles and behaviours too: obviously senior execs seem to be very excited at the opportunity to down-size and de-skill the workforce. Offshore and 
  using 
  LLMs - irresistable. By the time the terrible quality impacts delivery and maintainability - they'll be long gone, with their golden parachutes. Nice work if you can get it.
* But Product Managers, Engineering Managers and entrepreneurs: can all be programmers now - all can escape the tyranny of syntax. For society, this might be a good thing. Security, privacy, 
  AI-slop, and the dead internet might all get much worse however.
* Obviously, being a professional has always been more than just knowing syntax or a framework. Decades ago, Djikstra discussed the job being all about mental models and abstractions; and writing 
  the 
  code and mastering syntax is even less essential than ever. And indeed, no reason not to think a product manager can't have a good handle on this mindset.
* One topic that's interesting is the application to QA and tests: it's tempting to just get LLMs to write tests and move on but this misses the point of acceptance testing and the importance of 
  tests (& TDD obviously) as tools of design and clarity rather than as an 'after the fact' pro forma step. Good test come out of a sophisticated and accurate model of the system and the problem 
  domain: that's how you know where the edges of the edge cases are!
* This highlights one huge failing of LLMs for code: they can't form that overall mental model of a system. This type of understanding is most important in maintanance 
  legacy and novel code-bases and problems. I think this limitation is easily overlooked when dazzled by shiny 'hello world' demos: greenfield development is so refreshing and rapid!
* So given their tendancy to rush, fabulate and lie; How will the trade-off between 'quick' and 'done properly' play out? In a couple of years, will we look back at tons of LLM productivity and 
  shudder? A rat's nest of vibe-coded slapdash work? Will their be a backlash; new techniques and methodologies or just an accomodation and we'll just cope? Interesting to speculate
* Elegance - and intuition: these are somewhat aesthetic judgements but it's a measure of a good design: simplicity, clarity, maintainability; an elegant solution addresses all of these criteria. LLMs aren't tuned to this sentiment!
* Maybe we'll see them thrive in prototyping and some more cookiecutter tasks but become just a tool for senior devs on legacy production code. Exporing spikes and extracting valuable bits - very 
  handy!


Ok that's enough for now. Likely to add to this and come back to it as this exciting topic develops. Comments and feedback welcome.