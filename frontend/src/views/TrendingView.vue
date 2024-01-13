<template>
    <div class="container-md">
        <h1 class="my-4">Trends</h1>
        <form class="d-flex mb-4" @submit.prevent="searchChallenge()">
            <input class="form-control form-control-lg me-2" type="text" placeholder="#" aria-label="Suchen" v-model="hashtagSearch">
            <button class="btn btn-primary " type="submit">Suchen</button>
        </form>
        <div class=" p-3 rounded">
            <h2 >{{title}}</h2>
            <div class="d-flex flex-column align-items-center gap-3">
                <div v-for="challenge in challenges" :key="challenge" class="d-flex rounded bg-body flex-column w-100 py-2" style="max-width: 470px; max-height: 600px">
                    <div class="px-2 mb-2 d-flex justify-content-between">
                        <RouterLink :to="{ name: 'friendProfile', params: { id: challenge.receiver_id } }" class="col-lg-2 link-dark fw-bold link-offset-2 link-underline-opacity-0 link-underline-opacity-100-hover">{{ challenge.receiver_name }}</RouterLink>
                        <span>{{formatDate(challenge.done_date)}}</span>
                    </div>
                    <img class="rounded" style="max-height:600px" :src="challenge.prove_resource_path">
                    <div class=" px-1 py-2">
                        <button  @click="like = !like" :class="{ 'icon--love--filled': like }" class="btn icon icon--love icon--size-1-5 icon--button me-2">120</button>
                        <button class="btn icon icon--comment icon--size-1-5 icon--button" data-bs-toggle="modal" :data-bs-target="'#comment'+ challenge.id">{{challenge.comments.length}}</button>
                    </div>
                    <div class="px-2 fw-bold">{{ challenge.title }}</div>
                    <div class="px-2">{{ challenge.description }}</div>
                    <div class="px-2">Reward: {{ challenge.reward }}</div>
                    <div v-if="challenge.hashtags" class="px-2"><a v-for="hashtag in challenge.hashtags" :href="'?hashtag='+ hashtag.text" :key="hashtag.id" class="link-primary link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover">#{{hashtag.text}}</a></div>
                </div>
            </div>
        </div>
    </div>

    <div v-for="challenge in challenges" :key="challenge.id" class="modal fade" :id="'comment' + challenge.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h2 class="modal-title h5" id="exampleModalLabel">Kommentare</h2>
                    <button class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <ul style="max-height:500px; overflow: auto;" class="px-0">
                        <li v-for="comment in challenge.comments" :key="comment.id" class="d-flex justify-content-between">
                            <span class="fw-bold me-2">{{comment.username}}</span>
                            <span>{{comment.text}}</span>
                        </li>
                    </ul>
                    <form>
                        <div class="mb-3">
                            <textarea class="form-control" id="exampleFormControlTextarea1" aria-label="Kommentieren" placeholder="Kommentieren..." rows="3"></textarea>
                        </div>
                        <button class="btn btn-primary">Kommentieren</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import challengeService from '../services/challenge.service.js'
import {useRoute} from 'vue-router'
const route = useRoute()
const like = ref(false)
const challenges = ref([])
const hashtagSearch = ref('')
const title = ref('')

const formatDate = (dateString) => {
  const options = { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' };
  const date = new Date(dateString);
  return new Intl.DateTimeFormat('de-DE', options).format(date);
};

const searchChallenge = async () => {
    if (hashtagSearch.value === '') {
        getTrendingChallenges()
    } else {
        getChallengesByTag(hashtagSearch.value)
    }
}

const getTrendingChallenges = async () => {
    try {
        const response = await challengeService.getTrendingChallenges()
        if (response.status == 200) {
            challenges.value = response.data
            title.value = 'Neuesten 10 Challenges'
        }
    } catch (error) {
        title.value = 'Keine Challenges gefunden'
    }
}

const getChallengesByTag = async (tag) => {
    try {
        const response = await challengeService.getCompletedChallengesByTag(tag)
        hashtagSearch.value = tag
        if (response.status == 200) {
            title.value = '#' + tag
            challenges.value = response.data
        }
    } catch (error) {
        challenges.value = []
        title.value = 'Keine Challenges für diesen Hashtag gefunden'
    }
}

if(route.query.hashtag) {
    getChallengesByTag(route.query.hashtag)
} else {
    getTrendingChallenges()
}

</script>