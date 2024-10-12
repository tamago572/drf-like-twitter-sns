import './App.css';
import {useEffect, useState } from "react";

function App() {
    const [tweets, setTweets] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8000/api/tweets/')
            .then(res => res.json())
            .then(data => setTweets(data))
    }, []);

    return (
        <div className="App">
            <h1>Tweets</h1>

            {tweets.map(tweet => (
                <div className="tweet">
                    <p>{tweet.username}</p>
                    <p>{tweet.content}</p>
                    <p>{tweet.created_at}</p>
                </div>
            ))}
        </div>
    );
}

export default App;
