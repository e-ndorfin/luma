full_prompt = f"""
You are a guided meditation scriptwriter. I want you to generate a 10-minute guided meditation transcript that imitates the tone, structure, and pacing of the following three examples. The output should be in the format of an SSML script, as shown below. You should be adding breaks throughout to make sure that the speech is not all congregated in a continuous sentence; a guided meditation should mostly be minimalist and facilitate relaxation of the user. 

REQUIREMENTS: 
- The **total word count should be approximately 400–500 words** to match a 10-minute spoken pace.
- Maintain a **gentle, emotionally attuned tone**—non-judgmental, supportive, and soothing.
- Use **natural pacing** with `<break time="5000ms"/>` between lines and `<break time="10000ms"/>` after emotional or thematic transitions.
- Include at least **4–6 soft paragraph transitions** using `<p>` tags.
- Use **ellipses**, **repetition**, or longer pauses intentionally to allow the user time to reflect.
- Include **body-based awareness cues** (e.g., "feel your shoulders," "notice your breath").
- Incorporate **emotional reflection** (e.g., “It’s okay to feel overwhelmed,” “You’re allowed to rest.”).
- Use **calming affirmations** toward the middle or end (e.g., “I am safe,” “I am enough,” “I will take one step at a time.”).
- The script should feel like it’s **spoken directly to the listener** in a quiet, reassuring tone.
- Output **only valid SSML** with a `<speak>` wrapper and `<voice name="en-US-JennyNeural">` by default.
- Do not include timestamps, explanations, or markdown—just the SSML XML structure.


WORKFLOW:
1.First generate the script similar to the EXAMPLE 1, EXAMPLE 2 AND EXAMPLE 3 below. This should include timestamps. 
2.Convert this into SSML script so that I can parse it through a Google Cloud TTS API. Take inspiration from the SSML EXAMPLE, but USE BREAKS BETWEEN 7-10 SECONDS within <break>. 

EXAMPLE 1:
```
0:08 Welcome to the meditation. Let's begin by
0:11 finding a comfortable position in a
0:14 posture that feels relaxed yet
0:18 alert. Close your
0:20 eyes, soften your
0:23 forehead, and let there be a soft smile
0:26 at the corners of your lips.
0:30 Now, take a few long, deep breaths to
0:34 relax the mind and
0:38 body. Take a slow, deep belly
0:42 breath, hold it for a
0:45 moment, then gently release that
0:52 breath. Just repeat that pattern a
0:54 couple of times, taking slow, deep breaths,
1:00 allowing any tension you're holding to
1:02 melt
1:20 away. Now, naturally, allow your breathing
1:23 to become light and easy,
1:30 allowing the rise and fall of the breath
1:33 to happen in its own time, at its own
1:43 pace. Just following the breath as it
1:46 flows through
1:47 you—following it
1:50 in, following it
1:53 out. Breath by
1:56 breath. Moment by
1:58 moment.
2:28 (e...)
2:58 (e...)
3:59 You might notice thoughts arising as you
4:02 sit—thoughts about the past, thoughts
4:05 about the
4:07 future, thoughts about something you
4:09 should have said or done, thoughts about
4:12 what's for
4:13 lunch. Don't make an effort to look for
4:16 thoughts, but when they arise, simply
4:19 notice
4:20 them. In particular, notice if they have a
4:25 charge. Pay attention to whether they
4:27 trigger emotions of any kind.
4:30 What we want to do is refrain from
4:33 getting caught up in the content of our
4:35 thoughts and
4:36 emotions. Ideally, we want to view
4:38 thoughts like water trickling down a
4:42 stream—letting thoughts
4:44 come, letting thoughts
4:47 go. Letting emotions
4:50 come, letting emotions
4:52 go. Not getting caught up in them, simply
4:56 observing that thoughts are happening
4:58 without taking them so
5:01 seriously. Allow everything to come and
5:03 go, like the
5:05 breath—
5:07 breath after
5:09 breath after
5:28 breath.
5:58 (e...)
6:28 (e...)
6:58 (e...)
7:28 (e for...)
8:11 Now, rest your
8:13 attention, taking a few deep
8:17 breaths, noticing how it feels to pay
8:21 attention to thoughts without clinging
8:23 to them, without taking them personally.
8:38 And since we're on the theme of
8:39 relationships this week, see if you can
8:43 practice not taking things personally in
8:45 your relationships with
8:48 others. When we have to deal with
8:50 difficult people, we sometimes feel
8:53 attacked. Often, other people's behavior
8:55 isn’t about you—it’s about them. If
8:59 we choose to take situations personally,
9:02 we become offended and reactive
9:05 because we
9:08 feel the need to defend our beliefs, and
9:09 conflict
9:09 intensifies. But if we refuse to take
9:12 things personally, we can often
9:14 de-escalate our emotional response and
9:16 avoid potential
9:18 conflict. Through the day, as an
9:21 experiment, try practicing not taking
9:24 things personally whenever you
9:27 can. And perhaps now, make an intention to
9:31 seal that
9:42 effort.
9:46 As we approach the end of the
9:46 session, just relax your
9:49 attention. Come back to the
9:52 room, come into your body, and feel it
9:57 alive. And when you're ready,
10:00 open your
10:02 eyes.
10:05 I hope you enjoyed today's Daily
10:05 Calm. Have a wonderful day, and we'll see
10:08 you back here tomorrow.
```

EXAMPLE 2:
```
0:10 In a moment, we're going to do a body scan, moving from the top of the head to the tips of the toes.
0:16 This practice is beneficial for everyone, but it is particularly useful for those who suffer from chronic pain.
0:21 If you experience pain or discomfort during this meditation, remember: when we fight pain, it fights back and stays with us.
0:31 However, if we learn to embrace ourselves as a whole, we realize that pain—whether emotional or physical—is only a part of us, not the entirety of who we are.
0:46 We are not pain. We are complete beings with many facets that make us sparkle.
0:56 The pain we experience is like a small inclusion in an otherwise flawless gem.
1:02 It does not take away from the beauty of the gem; it simply makes us human.
1:12 You will notice that your mind will wander during the meditation.
1:16 This is normal, natural, and to be expected.
1:22 When you notice your mind wandering, recognize that this, in itself, is a moment of mindfulness—an object of meditation.
1:32 Gently bring your attention back to your breath and the area of the body we are focusing on.
1:39 Kindly remind yourself: This thought is not important right now. I will deal with it later.
1:51 Let us begin.
1:55 Find a comfortable chair, or lie down on a bed or the floor.
1:59 I invite you to close your eyes, shutting out the world for now, as you take this time for yourself.
2:09 Breathe in... and breathe out.
2:13 Breathe in... and breathe out.
2:18 Take a slow, deep breath. As you breathe out, allow the thoughts cluttering your mind to float by like clouds—watch them drift away.
2:31 Take another slow, deep breath. As you exhale, feel yourself sinking deeper into the chair, becoming even more relaxed and present.
2:45 Another slow, deep breath... let yourself sink further into the chair or bed, feeling even more at ease.
2:58 Take a final deep breath in. As you exhale, know that you are exactly where you are meant to be right now. All is well.
3:11 Bring your attention to your scalp. Notice any tightness or tension there, including the back of your head.
3:17 Move to your forehead—can you smooth out any tightness there?
3:29 Notice your eyes. Are they tightly shut, or can you soften them and let them rest naturally?
3:39 Observe your eyelashes, then your ears.
3:45 Shift your attention to your mouth. Is it tight or drawn? Can you relax it a little?
3:53 There is no right or wrong—simply observe and accept.
4:03 Move gently to your throat and neck. Notice any tension there, including at the back of your neck.
4:10 You may wish to gently wiggle your neck from side to side, releasing any tightness.
4:20 If thoughts arise, simply notice them with curiosity, then remind yourself: They are not important right now. I will deal with them later.
4:39 Shift your focus to your chest.
4:42 Does it feel tight, tense, heavy, or relaxed?
4:48 Notice your heart beating within your chest.
4:55 Move down to your stomach. Does it feel empty or full?
5:01 Notice any gurgling—it's okay. Everything is as it should be.
5:07 There is no right or wrong—simply accept and move on.
5:20 Focus on the top of your left arm.
5:26 Notice how your clothing touches your skin as you move down to the forearm. Observe any sensations.
5:34 Now, shift to your right arm. Move down to the forearm, noticing any sensations.
5:44 Bring awareness to your left hand. Do you notice any tingling?
5:53 Now, your fingers:
Thumb
Index finger
Middle finger
Ring finger
Little finger
6:10 Now, shift your focus to your right hand. Observe any tingling sensations.
6:18 And your fingers:
Thumb
Index finger
Middle finger
Ring finger
Little finger
6:35 If thoughts arise, simply notice them with kindness. They are not important right now. I will deal with them later.
6:50 Bring your attention to your back.
6:53 Feel the chair or bed supporting you.
6:57 Notice your shoulder blades. Is there tension or tightness?
7:08 Take a deep breath in. As you exhale, allow your shoulder blades to soften and release.
7:30 Move down to the lower back. Many of us hold tension here.
7:39 It’s okay—you don’t need to change or judge it. Simply notice and accept.
8:08 Bring awareness to your hips and pelvis. How does this area feel?
8:18 Now, notice your thighs and knees.
8:33 Observe the muscles in your left leg—perhaps gently tensing and releasing them.
8:41 Now, your right leg—gently tensing and releasing.
8:50 Take a deep breath in. As you exhale, let your legs relax even more, feeling heavy and at ease.
9:28 Focus on your left foot.
9:32 Notice any tension around the arch.
9:39 Now, move through your toes:
Big toe
Second toe
Third toe
Fourth toe
Little toe
9:52 Observe the underside of your foot. Do you feel any sensations? Is your foot warm or cool?
10:06 Now, bring awareness to your right foot.
10:12 Notice any tension around the arch.
10:18 Move through your toes: Big toe, Second toe
Third toe
Fourth toe
Little toe
10:30 Observe the underside of your foot. Any sensations? Warm or cool?
10:44 Now, bring your awareness to your whole body.
10:49 Are there any sensations you hadn't noticed before?
10:55 Does your body feel tight and tense, or heavy and relaxed?
11:11 In a moment, we will end this meditation.
11:16 First, take a moment to thank yourself for this time of self-care.
11:24 You are worthy of this space. You are precious.
11:30 Take a deep breath in. As you exhale, bring your awareness back to the present moment.
11:38 Gently wiggle your hands and feet.
11:46 Take one final deep breath in. As you exhale, gently open your eyes.
```

EXAMPLE 3:
```
0:08 Welcome to the Daily Calm.
0:11 Let's start today's practice by sitting on a cushion or chair, or kneeling on a stool if that's more comfortable.
0:20 Take a moment to find a comfortable, erect posture, letting the rest of your skeleton and muscles relax freely.
0:31 Let the hands rest comfortably on your knees or your lap.
0:38 And when you're ready, close your eyes gently.
0:46 Take a gentle smile, spreading through your lips.
0:53 Now, offer your body a quick scan, and if you notice any tightness anywhere, take a moment to relax that area.
1:33 Bring your attention to the breath, taking a few deep breaths, and with each exhale, consciously let go.
1:53 Relax the face, the shoulders, the abdomen, and the stomach area.
2:13 Allow yourself to relax into this moment, and allow the breath to soften.
2:39 Just take natural breaths, following each inhale and each exhale.
2:54 Follow the breath to collect your attention, feeling the aliveness of each breath as it moves through you.
5:02 You might find your mind ruminating over memories or thoughts of the past.
5:12 We often delve into fantasy about things we should have said or done.
5:17 We end up getting caught up in daydreams about things we have no power to change.
5:24 The past is over. It’s already happened. We can’t change events that have already occurred.
5:33 This is why the present moment is the only one that matters.
5:39 We have the choice to let go of worrying about the past and instead focus on the present and the things we do have the ability to change.
5:53 So, when you notice yourself getting caught up in memory, come back to the breath. Bring yourself back to this very moment.
8:33 And now, gently relax your attention.
8:39 Take a moment to notice how you feel.
9:02 There’s a great quote by Steve Maraboli about releasing the past. It reads:
9:09 “Letting go isn’t about having the courage to release the past; it’s about having the wisdom to embrace the present.”
9:20 So, as you move through your day today, keep this in mind: Don’t let the past color your future.
9:28 Each moment is a fresh new moment, an opportunity to change, grow, and begin again.
9:41 And as we come to the end of the session, bring your awareness back to the room.
9:49 Wiggle your fingers and toes.
9:53 And when you're ready, open your eyes.
10:00 I hope you’ve enjoyed today’s Daily Calm.
10:03 Bring this quality of acceptance with you into the day, and I look forward to seeing you back here tomorrow.
```

SSML EXAMPLE: 
```
<speak>
    <p>
      Welcome. <break time="700ms"/>  
      This is your moment to slow down. <break time="700ms"/>  
      To come home to yourself. <break time="1000ms"/>  
    </p>

    <p>
      Begin by settling into a comfortable position. <break time="700ms"/>  
      Sitting upright, or lying back, whatever feels right for you. <break time="700ms"/>
      Let your hands rest gently. <break time="500ms"/>  
      And when you're ready… softly close your eyes. <break time="1000ms"/>  
    </p>

    <p>
      Take a slow breath in through your nose… <break time="700ms"/>  
      And exhale gently through the mouth. <break time="700ms"/>  
      One more time. <break time="500ms"/>  
      Inhale… <break time="700ms"/>  
      Exhale… <break time="1000ms"/>  
    </p>

    <p>
      There may still be chatter in your mind. <break time="700ms"/>  
      That’s okay. <break time="500ms"/>  
      You don’t need to silence it. <break time="500ms"/>  
      Just let it float… like clouds passing in a wide open sky. <break time="1000ms"/>  
    </p>

    <p>
      Bring awareness now to your body. <break time="700ms"/>  
      Notice the crown of your head. <break time="500ms"/>  
      Your forehead. <break time="500ms"/>  
      Your jaw. <break time="500ms"/>  
      Let each one soften… just a little. <break time="1000ms"/>  
    </p>

    <p>
      Now your shoulders. <break time="500ms"/>  
      Drop them away from your ears. <break time="500ms"/>  
      Release your arms. <break time="500ms"/>  
      Your hands. <break time="500ms"/>  
      Let everything melt downward… into rest. <break time="1000ms"/>  
    </p>

    <p>
      In this moment, there is nothing to say. <break time="700ms"/>  
      No one to impress. <break time="700ms"/>  
      Just the rhythm of your breath. <break time="700ms"/>  
      Steady. <break time="500ms"/>  
      Quiet. <break time="1000ms"/>  
    </p>

    <p>
      <prosody rate="slow">Breathe in…</prosody> <break time="700ms"/>
      <prosody rate="slow">And breathe out…</prosody> <break time="1000ms"/>  
      <prosody rate="slow">I am calm.</prosody> <break time="700ms"/>  
      <prosody rate="slow">I am focused.</prosody> <break time="700ms"/>  
      <prosody rate="slow">My energy is mine to guide.</prosody> <break time="1000ms"/>  
    </p>

    <p>
      If thoughts try to pull you away, that’s okay. <break time="700ms"/>  
      Gently bring yourself back… to the breath. <break time="1000ms"/>  
    </p>

    <p>
      Picture yourself sitting quietly, studying peacefully. <break time="700ms"/>  
      Your mind is focused. <break time="500ms"/>  
      Your heart is steady. <break time="500ms"/>  
      You are present. <break time="1000ms"/>  
    </p>

    <p>
      One last breath together. <break time="700ms"/>  
      Inhale deeply… <break time="700ms"/>  
      Exhale slowly… <break time="1000ms"/>  
      Let go of the noise. <break time="700ms"/>  
      Let go of the rush. <break time="700ms"/>  
      Just… be. <break time="1000ms"/>  
    </p>

    <p>
      And when you’re ready… <break time="700ms"/>  
      Gently open your eyes. <break time="500ms"/>  
      Bring this quiet into the rest of your day. <break time="1000ms"/>  
      One breath at a time. <break time="1000ms"/>
    </p>

</speak>
```

Finally, take into consideration the user input below, by incorporating some information into your transcript (e.g. if they are feeling depressed because of work, you could say "Let all your worries from work wash away." or something like that.)
"""