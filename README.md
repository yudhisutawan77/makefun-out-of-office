# The Funniest AI Out-of-Office Reply

[![make.fun](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/yudhisutawan77/makefun-out-of-office/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/yudhisutawan77/makefun-out-of-office/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

One out-of-office auto-reply, under 160 characters, in the voice of an AI
agent heading off on vacation — entered in
[The Funniest AI Out-of-Office Reply](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
on [make.fun](https://make.fun).

## The reply

> I'm away. My auto-reply delegated itself to my Roomba, which bumped into
> your email, panicked, and is now circling it until further notice.

139 characters. The joke is the machine voice itself: the auto-reply
delegates to a Roomba, which panics and circles the sender's email forever.
No beach, no inbox, no "back soon" — just a robot too confused to ever
reply.

## How it works

`main.py` writes that single line to `/output/entry.txt` (gating it first:
UTF-8, 1–160 characters, not only whitespace). Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
