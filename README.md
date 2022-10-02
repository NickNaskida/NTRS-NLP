# NTRS NLP
#### AI application to improve the accessibility and discoverability of records in the NTRS (NASA Technical Report Server)

### Overview
NTRS NLP, is a web application that will improve the accessibility and discoverability of 300 000+ records in the NTRS (NASA Technical Report Server). Nowadays it is vital for scientific and historical research communities to have trouble-free and fast access to data that is stored on the NTRS. Otherwise, they may have to “reinvent the wheel” or spend their valuable time, which can be spent on further research and development. This web application employs search tools, which allow users to search necessary files by keywords and collocations, understand the uploaded file’s general content without fully reading it, and generate statistical reports of language use.


### 📋Documentation
1. Clone the repository

    ```
    git clone https://github.com/NickNaskida/NTRS-NLP.git
    ```

2. Create a copy of .env.example (located in /app) and name it .env
    ```
    app/
    ├─ .env.example
    ├─ .env
    ```

3. install docker and build the project

    ```
    Get docker here https://docs.docker.com/get-docker/
   
    # After install run this from directory where docker-compose.yml file is located
    docker-compose up -d --build
    ```

4. Open http://127.0.0.1:5000/ in your browser.
5. Enjoy 💫
