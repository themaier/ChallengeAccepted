<template>
    <div class="container-md">
        <h1 class="my-4">{{username}} - Abgeschlossene Challenges</h1>
        <div class="p-3">
            <div class="d-flex flex-column align-items-center gap-3">
                <div v-for="challenge in challenges" :key="challenge" class="d-flex rounded bg-body flex-column w-100 py-2" style="max-width: 470px; max-height: 600px">
                    <div class="px-2 mb-2 d-flex justify-content-between">
                        <span class="fw-bold">{{challenge.receiver_name}}</span>
                        <span>{{formatDate(challenge.done_date)}}</span>
                    </div>
                    <img class="rounded" style="max-height:600px" :src="challenge.prove_resource_path">
                    <div class=" px-1 py-2">
                        <button  @click="like = !like" :class="{ 'icon--love--filled': like }" class="btn icon icon--love icon--size-1-5 icon--button me-2">120</button>
                        <button class="btn icon icon--comment icon--size-1-5 icon--button" data-bs-toggle="modal" :data-bs-target="'#comment'+ challenge.id">{{challenge.comments.length}}</button>
                    </div>
                    <div class="px-2 fw-bold">{{ challenge.title }}</div>
                    <div class="px-2">{{ challenge.description }}</div>
                    <div v-if="challenge.reward" class="px-2">Reward: {{ challenge.reward }}</div>
                    <div v-if="challenge.hashtags" class="px-2"><a v-for="hashtag in challenge.hashtags" :href="'?'+ hashtag.text" :key="hashtag.id" class="link-primary link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover">#{{hashtag.text}}</a></div>
                </div>
            </div>
        </div>
    </div>

<CommentSection :challenges="challenges"></CommentSection>
</template>

<script setup>
import { ref } from 'vue'
import challengeService from '../services/challenge.service.js'
import {useStore} from '../stores/store'
import CommentSection from '../components/CommentSection.vue'

import { useRouter, useRoute } from 'vue-router'
import userService from '../services/user.service.js'

const route = useRoute()
const like = ref(false)
const store = useStore()
const challenges = ref([])
const username = ref('')

const formatDate = (dateString) => {
  const options = { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' };
  const date = new Date(dateString);
  return new Intl.DateTimeFormat('de-DE', options).format(date);
};

const getCompletedChallengesByUser = async (id) => {

    try {
        const response = await challengeService.getCompletedChallengesByUser(id)
        if (response.status == 200) {
            challenges.value = response.data
        }
    } catch (error) {
        challenges.value = []
    }
}

const getUsername = async (id) => {
    try {
        const response = await userService.getUser(id)
        if (response.status == 200) {
            username.value =  response.data.username
        }
    } catch (error) {
        username.value = ''
    }
}

getCompletedChallengesByUser(route.params.id)
getUsername(route.params.id)

</script>