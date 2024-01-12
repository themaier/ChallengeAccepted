import axios from 'axios';

const API_URL = 'http://localhost:8000/challenges/';

class ChallengeService {

    async createChallenge(challenge) {
        return await axios.post(API_URL, challenge).then(response => {
            return response
        })
    }

    async getPendingChallenges(id) {
        return await axios.get(API_URL + id + '/pending').then(response => {
            return response
        })
    }

    async getAcceptedChallenges(id) {
        return await axios.get(API_URL + id + '/accepted').then(response => {
            return response
        })
    }
};

export default new ChallengeService();