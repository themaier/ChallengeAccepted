import axios from 'axios';

const API_URL = 'http://localhost:8000/challenges';

class ChallengeService {

    async createChallenge(challengeName, friend, description, hashtags, reward, chatgpt_check) {
        return await axios.post(API_URL,
            {
                user_id: 1,
                challenge_name: challengeName,
                friend_id: Number(friend),
                description: description,
                hashtags: hashtags,
                reward: reward,
                chatgpt_check: Boolean(chatgpt_check),
            })
            .then(response => { return response })
    }
};


export default new ChallengeService();