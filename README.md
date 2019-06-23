# Test task - social_network
---
### Quick Start:
1. Clone the repo:
```
git clone git@github.com:Wasper256/social_network.git
```
2. Create `.env` configuraton file inside project directory. It should contain next variables: 
```
DATABASE_URL=postgres://network_db:pass@localhost/network_db

NUMBER_OF_USERS=3
MAX_POSTS_PER_USER=3
MAX_LIKES_PER_USER=3
```
3. Install Pipenv
```
    pip install pipenv
```

4. Activate Pipenv
```
    pipenv shell
```
5. Install dependency's
```
pipenv install 
```
6. Django start
```
    pipenv run migrate
    pipenv run collectstatic
    pipenv run runserver
```
7. Launch automated bot 
```
 pipenv run bot
```