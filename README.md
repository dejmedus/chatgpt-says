## ChatGPT Says 🤖👀

Train for the AI uprising by taking orders from ChatGPT!

Built for the [MLH API Week](https://ghw.mlh.io/challenges) Create your own API challenge.

#### Built with:

Python, Flask, Flask-Limiter, ChatGPT (who kindly provided the orders), Fly.io

#### Usage:

| Description                               | API Endpoint                                  |
| ----------------------------------------- | --------------------------------------------- |
| A random order                            | `/bot-says`                                   |
| Return order id 8                         | `/bot-says?id=8`                              |
| 10* random orders                         | `/bot-says?limit=10`                          |
| Random order from a specific category     | `/bot-says?category=humorous`                 |
| 5* random orders from a specific category | `/bot-says?category=world-domination&limit=5` |
| Return all orders                         | `/bot-says?limit=all`                         |

\* If limit request is higher than the actual amount, will return all orders.

```shell
# basic example
curl 'https://<domain>/bot-says'

# with parameters
curl 'https://<domain>/bot-says?category=wellbeing&limit=5'
```



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
