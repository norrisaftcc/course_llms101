```
================================================================================
                CSC-113 AI FUNDAMENTALS - INSTRUCTOR GUIDE v1.3
                         "The GitHub-First Survival Guide"
                              By: TeachTechTerry
                          Last Updated: 08/17/2025
                    Platform: IRL Classroom (GitHub-Enhanced)
================================================================================

ASCII art header:
   _____ _____ _____      __  __  ____  
  / ____|_   _|_   _|    /_ |/_ ||___ \ 
 | |      | |   | |       | | | |  __) |
 | |      | |   | |       | | | | |__ < 
 | |____  | |   | |       | | | | ___) |
  \_____| |_|   |_|       |_| |_||____/ 
                                        
  [TEACHING AI WITHOUT LOSING YOUR MIND]

================================================================================
TABLE OF CONTENTS
================================================================================

1.0 - BEFORE YOU START (READ THIS OR YOU'RE SCREWED)
2.0 - CHARACTER CREATION (Pre-Semester Setup)
3.0 - TUTORIAL LEVEL (Week 1 - GitHub Initiation)
4.0 - MAIN CAMPAIGN WALKTHROUGH (Weeks 2-8)
5.0 - BOSS FIGHTS (Crisis Management)
6.0 - HIDDEN MECHANICS (Stuff They Don't Tell You)
7.0 - SPEEDRUN STRATS (Daily Operations)
8.0 - 100% COMPLETION GUIDE (Assessment)
9.0 - NEW GAME+ (Next Semester Prep)
10.0 - CHEAT CODES & EXPLOITS (Emergency Protocols)

================================================================================
1.0 - BEFORE YOU START (READ THIS OR YOU'RE SCREWED)
================================================================================

Listen up, professor. This isn't your standard "pedagogical framework" BS. This 
is how you ACTUALLY run CSC-113 without wanting to quit academia by Week 3.

THE CORE GAMEPLAY LOOP:
- Students break things in GitHub
- You say "failure is just exercise"  
- They fix it and feel like gods
- Repeat 100x per semester
- Everyone gets hired

If you're reading this thinking "but I need to teach them real CS" - STOP. 
GitHub IS real CS. The AI stuff is just the excuse to teach professional 
workflows. By the end, they'll have better portfolios than most bootcamp grads.

MINIMUM SYSTEM REQUIREMENTS:
- GitHub account (duh)
- Patience of a saint
- Ability to say "delete the branch" without laughing
- Coffee. So much coffee.
- Backup AI accounts (they WILL hit rate limits)

THINGS THAT WILL INSTANTLY KILL YOUR RUN:
- Trying to teach Git commands before GitHub web interface
- Letting students commit directly to main
- Explaining what a DAG is
- Using the word "repository" before Week 2
- Showing a merge conflict before Week 4

================================================================================
2.0 - CHARACTER CREATION (Pre-Semester Setup)
================================================================================

=== WEEK -2: INITIAL SPAWN ===

Right, you've got 2 weeks before students show up. Here's the speedrun:

DAY 1 - GitHub Org Setup [CRITICAL PATH]
--------------------------------------
1. Create org: "csc113-fall-2025" or whatever
2. Make it PRIVATE (trust me on this)
3. Enable everything: Issues, Discussions, Projects, Wiki
4. Apply for education benefits NOW (takes 1-3 days)

   PRO TIP: Use a personal account to test student workflows. You'll find 
   broken stuff before they do.

DAY 2 - Template Repositories [DO NOT SKIP]
-------------------------------------------
You need EXACTLY four templates. No more, no less.

   student-portfolio-template/
   ├── README.md    <-- Their future resume
   ├── projects/    <-- Where the magic happens
   └── reflections/ <-- Where they pretend to learn

   EXPLOIT: Pre-populate with example content. Students who "forget" to 
   change it are instantly caught.

DAY 3 - Protection Rules [SAVES YOUR SANITY]
--------------------------------------------
Main branch protection on EVERYTHING:
   [x] Require PR reviews
   [x] Dismiss stale reviews  
   [x] Up-to-date with main
   [x] Include administrators (yes, even you)

   WARNING: Students WILL try to force push. This stops them.

=== WEEK -1: LOADING RESOURCES ===

DAY 1 - AI Services Setup [UPDATED AUGUST 2025]
-----------------------------------------------
Primary: Gemini 2.5 Flash (the new hotness)
   
   FREE TIER REALITY CHECK:
   - 10 requests/minute (RPM)
   - 500 requests/day (RPD)
   - After 10-15 prompts, downgrades from Pro to Flash
   - 250,000 tokens/minute (seems generous but isn't)
   
   PAID TIER (when they inevitably need it):
   - 1000 RPM / 10,000 RPD
   - Still cheaper than therapy

   NEW PLAYER: Gemini 2.5 Flash-Lite
   - $0.10 input / $0.40 output per 1M tokens
   - For when Flash is too expensive
   - Performance hit but wallet survives

Backup Stack:
   1. Claude (free tier - still exists somehow)
   2. ChatGPT (free tier - slower than dial-up)
   3. Local Ollama (for the desperate)
   4. "The AI is rate-limited, use paper"

   CHEESE STRAT: Create "Kevin from IT" as a Copilot persona. Students love
   Kevin. Kevin never judges their terrible code. Kevin just got more expensive
   but still cheaper than a TA.

   HIDDEN MECHANIC: "Thinking Budget"
   - Gemini 2.5 now thinks before responding
   - You can control how much (0-24,576 tokens)
   - Set to 0 for speed, max for "please actually work"
   - Students won't understand this. That's fine.

DAY 2 - NPC Recruitment (Community Partners)
--------------------------------------------
You need 3-5 local businesses/nonprofits as "quest givers"

Email template that actually works:
   "Students will solve a real problem for you.
    Time needed: 2 hours total.
    You get: Free consulting and fresh perspectives.
    We get: Real projects for portfolios."

   HIDDEN STAT: Partners who've hired students before give 2x better projects

DAY 3 - Tutorial Documentation
------------------------------
Host everything on GitHub Pages. Students can't claim "I couldn't find it"
when it's literally in the org they visit daily.

   SECRET: Make the URL a rickroll first, change it Day 1. Ice breaker gold.

================================================================================
3.0 - TUTORIAL LEVEL (Week 1 - GitHub Initiation) 
================================================================================

=== DAY 1: "HELLO WORLD" (BUT GITHUB) ===

Your opening cutscene (say this verbatim):
------------------------------------------
"Hello, Scholars! Before we touch AI, we're learning how every tech company
on Earth actually works. This isn't homework - this is literally how I'd 
submit code at Google."

THE LIVE DEMO SEQUENCE:
1. Create repo (call it "my-terrible-first-repo")
2. Create Issue: "Add introduction because I exist"
3. Create branch: "1-add-intro"
4. Edit README in browser (NO COMMAND LINE YET)
5. Commit: "Add brilliant introduction"
6. Open PR: "Fixes #1 - I exist now"
7. Merge it
8. Celebrate like you just beat Dark Souls

COMMON STUDENT REACTIONS:
- "This seems like a lot of work" -> "Yes, that's the point"
- "Can't I just email you?" -> "Would you email Google your code?"
- "I already know Git" -> "Cool, you can help others"

SUCCESS METRICS:
- 100% have GitHub accounts: Required
- 80% created first repo: Expected  
- 60% understand what happened: Good enough
- 40% think you're insane: Perfect

=== DAYS 2-5: THE DAILY STANDUP RITUAL ===

Every. Single. Day. Starts. Like. This:

```
YOU: "Standup time! 30 seconds each. What'd you do, what're you doing, 
      what's blocking you?"
THEM: *panic*
YOU: "Sarah, you're up!"
SARAH: "I... made commits?"
YOU: "What kind of commits?"
SARAH: "The... good kind?"
YOU: "Good enough! Next!"
```

By Day 5, they'll actually give real updates. It's beautiful.

INTERVENTION FLOWCHART:
                    Did they speak in standup?
                           /        \
                         NO          YES
                         |            |
                  Check in after   Did they commit?
                       class        /        \
                                  NO          YES
                                  |            |
                           "Show me where   "Great work!"
                            you're stuck"

================================================================================
4.0 - MAIN CAMPAIGN WALKTHROUGH
================================================================================

=== WEEK 2: THE ASSISTANT FACTORY ===

This week they build "Kevin Jr." - their first AI assistant.

DAILY RAID BOSSES:
- Monday: "My prompt doesn't work" (Solution: iterate)
- Tuesday: "Kevin won't respond" (Solution: check format)
- Wednesday: "I hit rate limits" (Solution: Flash-Lite exists)
- Thursday: "Can I start over?" (Answer: always yes)
- Friday: "Look what Kevin can do!" (Victory lap)

THE RATE LIMIT MINIGAME:
- Students start confident with free tier
- Hit 10 prompts, get downgraded to Flash
- Panic ensues
- "Welcome to real development constraints!"
- Introduce Flash-Lite as the poverty option

YOUR SUPPORT ROTATION:
Morning: Check GitHub dashboard (5 min)
- Anyone stuck on same Issue for 3+ days?
- Any PRs waiting for review?
- Any branches named "asdfasdf" or "test"?

During Class: Circulate every 10 minutes
- Look for the "staring at screen" pose
- Check for the "rapid deletion" panic
- Listen for the "whispered cursing" phase
- Watch for "rate limit rage face"

Evening: Quick PR approvals (10 min)
- Approve anything that works
- Comment on anything creative
- Fix anything on fire

=== WEEKS 3-6: THE SPECIALIZATION SPLIT ===

Students self-select into character classes:

PROMPT MASTERS (The Wizards)
- Weapon: Natural language
- Armor: Google AI Studio (500 req/day)
- Special ability: Make AI do impossible things with words
- Weakness: "It's not real programming"
- Secret technique: Thinking budget manipulation

CODE BUILDERS (The Warriors)  
- Weapon: Python
- Armor: Google Colab
- Special ability: Actually understand what's happening
- Weakness: Spend 3 hours automating 5-minute task
- Ultimate: Direct API calls with proper error handling

CHAOS AGENTS (The Wild Cards)
- Weapon: Whatever works
- Armor: Borrowed code
- Special ability: Somehow it works
- Weakness: Nobody including them knows how
- Legendary drop: Accidentally discover new exploits

YOUR JOB: Keep all three classes viable. No tier lists allowed.

PARTY COMPOSITION (Week 5):
Force mixed-class teams for community projects:
- 1 Prompt Master (requirements gathering)
- 1 Code Builder (technical implementation)  
- 1-2 Chaos Agents (testing/documentation/vibes)

=== WEEKS 7-8: THE FINAL BOSS RUSH ===

Community Partner Presentations (The Real Test)

PRESENTATION DAY LOADOUT:
- [ ] Backup laptop (someone's will die)
- [ ] Backup internet (hotspot ready)
- [ ] Backup projector adapter (every type)
- [ ] Coffee for partners
- [ ] Tissues for emotional students
- [ ] Camera for LinkedIn posts

THE PRESENTATION META:
- 7 minutes max (use a timer, be ruthless)
- 3 minutes Q&A (cut off investors who monopolize)
- 2 minute transition (they need it)
- Partners love: Working demos
- Partners hate: Theory without application

================================================================================
5.0 - BOSS FIGHTS (Crisis Management)
================================================================================

=== BOSS: GEMINI RATE LIMITS (NEW IN 2025) ===
HP: 500 requests/day
STRATEGY: Teach resource management

PHASE 1: "Why is it suddenly slower?"
PHASE 2: Discover Pro downgraded to Flash
PHASE 3: Introduce Flash-Lite
PHASE 4: "This is why we cache responses"
PHASE 5: Learn to work within constraints

DROPS: Understanding of real-world limitations

=== BOSS: GITHUB IS DOWN ===
HP: ∞ (you can't hurt it)
STRATEGY: Pivot immediately

PHASE 1: Check status.github.com
PHASE 2: Announce calmly (don't panic)
PHASE 3: Switch to paper prototyping
PHASE 4: "This is why we have backups"
PHASE 5: Resume when it's back

DROPS: War story for future classes

=== BOSS: STUDENT HAVING BREAKDOWN ===
HP: Handle with care
STRATEGY: Compassion + practical help

YOUR COMBO:
1. "Let's take a breath"
2. "Show me where you're stuck"
3. "We'll fix this together"
4. Delete their branch
5. Start fresh
6. "See? Just exercise"

NEVER SAY:
- "It's easy"
- "Everyone else got it"
- "You should have started earlier"
- "Just use Flash-Lite" (when they're already frustrated)

=== BOSS: THE ACADEMIC PURIST ===
HP: 1000 (regenerates with every complaint)
ATTACKS: "This isn't real CS", "GitHub is just a tool", "Where's the theory?"

YOUR COUNTER-COMBO:
1. Show last semester's hired students
2. Pull up Google's engineering practices
3. Display student portfolio examples
4. "Feel free to observe final presentations"
5. They usually retreat

================================================================================
6.0 - HIDDEN MECHANICS (Stuff They Don't Tell You)
================================================================================

THE COMMIT MESSAGE EVOLUTION:
Week 1: "stuff", "fixed", "asdf"
Week 3: "updated code"
Week 5: "added button to homepage"
Week 8: "feat: implement responsive nav with accessibility support"

You don't teach this. It just... happens.

THE PEER REVIEW QUALITY CURVE:
Week 2: "looks good"
Week 4: "maybe add comments?"
Week 6: "I love the error handling in lines 34-47, but consider..."
Week 8: Better than your reviews

THE KEVIN REVELATION:
Around Week 5, someone realizes Kevin is just Copilot with a personality.
Your response: "Kevin's been Copilot all along. You've been learning prompt
engineering without realizing it."
Mind. Blown.

THE THINKING BUDGET DISCOVERY:
Week 6: "Why is the AI sometimes smart and sometimes dumb?"
You: "Let me introduce you to thinking budgets..."
Them: "We can control its brain power??"
You: "With great power comes great token costs"

SECRET TECHNIQUE: THE STRATEGIC IGNORE:
Some problems solve themselves if you wait 24 hours:
- "I can't push to main" (good, that's the point)
- "My PR has conflicts" (they'll figure it out)
- "Kevin won't write my entire project" (working as intended)
- "I hit rate limits" (welcome to the real world)

================================================================================
7.0 - SPEEDRUN STRATS (Daily Operations)
================================================================================

THE 30-MINUTE MORNING ROUTINE:
- 5 min: Check GitHub notifications
- 5 min: Scan Discord/Slack for panic
- 10 min: Review/approve simple PRs
- 5 min: Update daily standup notes
- 5 min: Coffee and existential acceptance

THE ANY% TEACHING ROUTE:
1. Standup (5 min)
2. Micro-lecture (10 min max)
3. "Go build something" (30 min)
4. Circulate and support (continuous)
5. "Commit before you leave!" (last 5 min)

OPTIMAL INTERVENTION TIMING:
- Too early: They don't learn
- Too late: They give up
- Just right: After 2 failed attempts
- Exception: If they're about to rm -rf /
- New exception: If they're burning through paid API credits

THE GRADE CALCULATION SPEEDRUN:
```python
grade = (
    has_github_portfolio * 30 +
    can_explain_their_work * 30 +
    helped_classmates * 20 +
    didnt_break_production * 10 +
    managed_rate_limits * 10  # NEW IN 2025!
)
```

================================================================================
8.0 - 100% COMPLETION GUIDE (Assessment)
================================================================================

ACHIEVEMENT LIST:
□ First Commit (5 pts) - Everyone gets this
□ Issue Creator (10 pts) - Made 10+ Issues
□ Review Master (15 pts) - Gave helpful PR feedback
□ Branch Wizard (10 pts) - Never committed to main
□ Collaboration King (20 pts) - Successful team project
□ Portfolio Complete (20 pts) - Professional GitHub profile
□ Community Impact (20 pts) - Partner loved their solution

HIDDEN ACHIEVEMENTS:
□ Helped classmate at 11 PM in Discord
□ Taught the class something you didn't know
□ Made Kevin do something unexpected
□ Recovered from complete disaster
□ Survived rate limit apocalypse
□ Discovered Flash-Lite before instructor mentioned it
□ Got hired before graduation

GRADING RUBRIC (REAL TALK):
A: Has portfolio, can explain it, helped others, managed resources
B: Has portfolio, can mostly explain it, hit some rate limits
C: Has portfolio, constantly rate limited
D: Tried (but burned through credits)
F: Didn't show up

================================================================================
9.0 - NEW GAME+ (Next Semester)
================================================================================

THINGS TO KEEP:
- Working templates (they're gold now)
- Partner contacts who were awesome
- Student success stories (with permission)
- Your sanity preservation techniques
- The good Kevin prompts
- Rate limit management strategies

THINGS TO PATCH:
- Whatever broke in Week 4 (something always does)
- The assignment everyone hated
- Timing that didn't work
- Tech that got deprecated (looking at you, Gemini 3.0)
- Your caffeine tolerance
- API budget allocation advice

VERSION 2.0 FEATURES:
- Pre-semester GitHub bootcamp (optional)
- Advanced track for returning students
- More partners (they talk to each other)
- Better crisis management docs
- Emotional support channel in Discord
- "Managing AI Costs" workshop (now mandatory)

================================================================================
10.0 - CHEAT CODES & EXPLOITS
================================================================================

THE INSTANT ENGAGEMENT CODE:
"Your assignment: Make an AI that does your homework in other classes.
Document everything in GitHub. Stay within free tier limits."

THE PANIC BUTTON:
When everything breaks: "Class, today we're doing AI Ethics Discussion."
Buys you time to fix stuff and saves API credits.

THE MOTIVATION EXPLOIT:
"Former student just got hired at [BIG COMPANY]. They said this course's
GitHub portfolio got them the interview. Also, they never exceeded free tier."
(Keep a list of success stories for this)

THE BUDGET HACK:
"Flash-Lite isn't worse, it's just... different. Like diet soda."
When they complain: "Professional developers optimize for cost daily."

THE FINAL CHEAT:
When a student says they can't do it:
"Show me your first commit from Week 1.
Now show me what you built yesterday.
You've already done the impossible.
And you did it on a student budget."

================================================================================
CREDITS & LEGAL
================================================================================

Written by: TeachTechTerry
Thanks to: Every student who broke something and taught me patience
Special thanks to: Kevin from IT (now with thinking mode!)
Extra special thanks to: Gemini Flash-Lite (poverty edition MVP)

This guide is released under the "Please Don't Sue Me" license. Share it,
modify it, print it and burn it for warmth, whatever. Just help other
instructors survive this course.

If this guide helped you, leave a review on... wait, wrong platform.

Remember: We're not teaching them to code. We're teaching them to learn.
The AI stuff is just the McGuffin. The real treasure was the GitHub 
portfolios we made along the way (within rate limits).

FINAL WISDOM:
"Failure is just exercise. Delete the branch and try again.
 Also, Flash-Lite exists when you're broke."
- Ancient Instructor Proverb (Updated for 2025)

================================================================================
END OF FILE - GO TEACH SOMETHING AWESOME (AFFORDABLY)
================================================================================
```