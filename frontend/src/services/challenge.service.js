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

    async acceptChallenge(id) {
        return await axios.put(API_URL + id + '/accept').then(response => {
            return response
        })
    }

    async declineChallenge(id) {
        return await axios.put(API_URL + id + '/decline').then(response => {
            return response
        })
    }

    async getCompletedChallengesByUser(id) {
        return await axios.get(API_URL + id + '/done').then(response => {
            return response
        })
    }

    async getCompletedChallengesByTag(hashtag) {
        return await axios.get(API_URL + hashtag).then(response => {
            return response
        })
    }

    async getTrendingChallenges() {
        return await axios.get(API_URL + 'latest/' + 10).then(response => {
            return response
        })
    }

};

export default new ChallengeService();