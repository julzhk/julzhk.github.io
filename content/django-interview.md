Title: Django Interview
Date: 2024-12-01
Category: Developer
Tags: Python, Data, Django
Author: Julz

## Django Interview Question

There was recently a question on Reddit that (to paraphrase) asked: 'I need to interview for a Django developer but I don't know anything about Django. What should I ask?'

I've hired a few Django (& other) devs and the majority of the hires worked out great, so I thought I'd share some thoughts on an approach.

### Have an explicit goal to each round of interview

The first things to do is to make the interview purposeful: Let's assume the attitude and personality testing stuff is covered elsewhere. Let's assume we have verified that their resume is 
more-or-less accurate – these being steps covered in other stages.

### Django Interview Purpose

So this round should be to tell if what the candidate says they can do is actually true; and is that at a skill at a level required?

It'd be an obvious to ask about concepts or define terms - but this can be a bit easy to game: I've thought some candidates were 'talk the talk, but not walk the walk' types. All it takes is a good 
memory;
or 
luck. So I'd 
avoid this line of 
enquiry. Besides it takes too long for an interview; it's very stressful and just doesn't provide much 'signal', imho.

Instead, I focus in on practical exercise: what is their approach to making a data model? This is a nice way to see if they actually have the experience they claim; they can think through a problem; 
and 
see if 
they can 
communicate 
clearly. BTW I thinks it's important to share the rubric up-front: eg: this isn't about getting the 'right' answer; it's about the process. That it's be a conversation about design and developer 
approach; it's not a test and so on.

This approach (and type of question) happily 
works 
for a variety of skill 
levels: A junior developer might convey the basic idea (and show themselves to have an open to learning attitude); while a more senior developer should identify the traps and the pitfalls!

### Model a nested to-do list?

It can be any simple data modelling question but I like: 'Design a data model for a nested to-do list'. There's plenty of other similar scenarios: 'a forum with nested comments'; 'a friends list';

We'll go with the 'nested to-do list' for this example - and it's a good balance of 'simple enough to discuss in a sitting' and 'trickier than it seems!' to get some juice out of the interview!

A candidate should ask (or be prompted, if they're junior) questions around: how many levels of nesting there will be?; are there any restrictions on number of items at each level?; how 
many users?, 
how 
many 
to-do lists per user? and so on... This can lead to a somewhat typical open-ended discussion on trade-offs and efficiency and some insight on system design priorities. This question is pretty good 
for all languages and frameworks; but I think Django's ORM makes it particularly approachable. It's useful for front-end developers too: Modelling a data structure properly in the FE is just as 
necessary as in backend. 

### Why is it tricky?

Well, the nested business means the data model can't be a simple structure: it's going to have a self-referential component. Of course, this is Django so we'll use the ORM: so do we have a `list` 
with many children foreign-key related `to-do items`? This would be a good start, but we have to consider the nesting. It all starts to get a bit tangled.

Better - and simpler - is to give `to-do items` a foreign key to themselves. This means `to-do item`s have as a parent another `to-do item`. A to-do list is just a `to-do item` with a null 
parent. We can track 'depth' of the item by counting the number of parents; it may be convenient to store this in the model too.

### And how would you make a REST API for this data model?
The question can lead to implementation thoughts on what a REST API for this data model would look like. Again, this should lead to an open-ended discussion. If they bring up HTMX or GraphQL, 
that's an interesting (and permitted) solution too of course.

Experienced developers will have the experience to discuss security; HTTP methods; statefulness; versioning the API future-proofing; and more. Do they consider getting the whole data for a nested 
to-do in one go - or just the top level?; how would they handle pagination; authentication; permissions; versioning. So lots of quite interesting topics to discuss.

A more junior developer might be stumped by many of 
these 
concerns; 
but they should be able to immediately grasp the reason why these things are important as soon as they're raised.

### Maintainable code

If there's time (and there can be if the interview's long enough), it's possible to actually get the candidate to build some of this in Django; it can allow insights into maintainability and 
bring up a 
discussion on test-driven development; SOLID principles and so on. 

### Summary

Obviously a coding interview is stressful to the candidate but at least it's more of a 'guided conversation' rather than a grilling - which I think is a lot less intimidating.

If the candidate's made 
these kind of things before (and they 
should have if they're a genuine Django candidate) then it should really be a breeze to come up with something workable. They might be time-pressured (stress and being interviewed makes candidates 
forget things) but that's okay; the 
goal 
isn't to finish the project. They might not get the finer details; but this gives some context to judge one candidate against another: My experience is that candidates diverge quite a lot in their 
ability to tackle the problem; and that's allows it to be a discerning factor.

### Conclusion

So that's one set of interesting questions to ask in a Django interview. It would be a single aspect of a more rounded process of course; but I do think it's necessary to have some 'hands-on' 
coding-based enquiry for a developer job - that isn't just on a 'whiteboard'; or trivia / 'gotcha' questions; but is actually something of a practical exercise that's at least relevant to the job 
of a Django developer. Needless to say, there's more to the job than just this; but in an hour - or two - we've got to gain some indications; and we have to start somewhere! 