## ChatGPT Says 🤖👀

Practice for the AI uprising by taking orders from ChatGPT!

#### Usage:

**URL: https://dejmedus.github.io**

| Description                               | API Endpoint                                  |
| ----------------------------------------- | --------------------------------------------- |
| A random order                            | `/bot-says`                                   |
| Return order id 8                         | `/bot-says?id=8`                              |
| 10 random orders                          | `/bot-says?limit=10`                          |
| Random order from a specific category     | `/bot-says?category=humorous`                 |
| 5* random orders from a specific category | `/bot-says?category=world-domination&limit=5` |
| Return all orders                         | `/bot-says?limit=all`                         |

```shell
# basic example
curl 'https://dejmedus.github.io/bot-says'

# with params
curl 'https://dejmedus.github.io/bot-says?category=humorous&limit=5'
```

\* If limit request is higher than the actual amount, will return all orders.


#### Categories:

`health` `wellbeing` `humorous` `ridiculous` `productivity` `mindfulness` `creativity` `gratitude`  `joy`  `affirmations` `learning`  `coding`  `nonsensical` `world-domination` `golden-rule`

#### Example Response:

```
{
    "id": 8,
    "chatgpt_says": "Say 'I love chatbots!' in a robot voice.",
    "category": {
        "id": 4,
        "name": "Ridiculous"
    }
}
```

✨ **Disclaimer:** ChatGPT notes that *"These are purely humorous and not intended to encourage or promote any negative actions (including the creation of an army of robotic cats)."*