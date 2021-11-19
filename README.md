# Url Shortener
* Services that generates a shorter unique alias for Urls.

## Made with:
* [Python-3.8/Django](https://www.djangoproject.com/)
* [Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)
* [Redis](https://redis.io/)
* [Sqlite](https://www.sqlite.org/index.html)
* [Docker](https://www.docker.com/)

## Get Started
### Setup
#### Docker
* Clone the repository
    ```sh
    $ git clone https://github.com/Xerrex/url_shortener.git
    ```

* Change into the cloned directory
    ```sh
    $ cd url_shortener
    ```
* Create '.env.db' & '.env.dev' envrionment variables
    ```sh
    $ cp examples.envfiles/examples.env.db .env.db
    $ cp examples.envfiles/examples.env.dev .env.dev
    ```
* update the Vaules on the .env.* files

* Start the docker containers
    ```sh
    $ docker-compose up -d --build
    ```
* Create super user
    ```sh
    $ docker-compose exec web python manage.py createsuperuser
    ```

### Usage
- Open [localhost:8000](http://localhost:8000/) to access the app.
- To view the database open [localhost:8080](http://localhost:8080/)
    * use the credentials defined in '.env.db'

## License
Distributed under the MIT License. See `LICENSE.txt` for more information.
