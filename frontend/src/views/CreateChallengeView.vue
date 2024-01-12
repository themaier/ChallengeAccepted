<template>
<main>
<div class="container-md">
  <h1 class="my-4">Challenge erstellen</h1>
    <div class="col-md-5 col mt-5 m-auto">
        <form @submit.prevent="createChallenge" novalidate :class="{'was-validated': needsValidation}" class="needs-validation">
            <div class="mb-3">
                <label class="form-label" for="challengename">Challenge Name *</label>
                <input class="form-control" id="challengename" required type="text" v-model="challenge.challenge_name" placeholder="z.B. Spexen" />
                <div class="invalid-feedback">
                  Challenge Name muss befüllt sein.
                </div>
            </div>
            <div class="mb-3">
              <label class="form-label" for="friend">Freund auswählen *</label>	
                <select id="friend" class="form-select" required v-model="challenge.friend_id" aria-label="Default select example">
                  <option disabled value="">Wähle einen Freund aus</option>
                  <option v-for="friend in friends" :key="friend.user_id" :value="friend.user_id">{{ friend.username }}</option>
                </select>
                <div class="invalid-feedback">
                  Freund muss ausgewählt sein.
                </div>
            </div>
            <div class="mb-3">
                <label for="description">Beschreibung *</label>
                <input type="text" class="form-control" required id="description" v-model="challenge.description">
                <div class="invalid-feedback">
                  Challenge Beschreibung muss befüllt sein.
                </div>
            </div>

            <div class="mb-3">
                <label for="hashtags">Hashtag (optional)</label>
                <input type="text" class="form-control" id="hashtags" v-model="challenge.hashtags_list" aria-describedby="hashtagHelp">
                <div id="hashtagHelp" class="form-text">
                  Hashtags müssen mit Komma getrennt werden und dürfen keine Leerzeichen sowie # enthalten.
                </div>
            </div>

            <div class="mb-3">
                <label for="reward">Reward (optional)</label>
                <input type="text" class="form-control" id="reward" v-model="challenge.reward">
            </div>
            <div>
              <label for="chatgpt_check">ChatGPT</label>
              <input type="checkbox" id="chatgpt_check" v-model="challenge.chatgpt_check">
            </div>
            <button type="submit" class="btn btn-primary" >Freund herausfordern</button>
            <div v-if="errorMessage != ''" class="mt-1 text-danger">{{errorMessage}}</div>
            <div v-if="successMessage != ''" class="mt-1 text-success">{{successMessage}}</div>
        </form>
    </div>
</div>
</main>
</template>

<script setup>
import {ref} from 'vue'
import challengeService from "../services/challenge.service.js";
import userService from "../services/user.service.js";
import friendshipService from "../services/friendship.service.js";
import {useStore} from '../stores/store'
const errorMessage = ref('')
const successMessage = ref('')
const needsValidation = ref(false)
const store = useStore()
const challenge = ref({
    user_id: store.user.id,
    challenge_name: '',
    friend_id: null,
    description: '',
    hashtags_list: null,
    reward: null,
    chatgpt_check: false,
  });

const friends = ref('')

const createChallenge = async () => {
  try {
    needsValidation.value = true

    if(!challenge.value.challenge_name || challenge.value.friend_id == null || !challenge.value.description){
      return
    }
    if (challenge.value.hashtags_list === '') challenge.value.hashtags_list = null
    if (challenge.value.reward === '') challenge.value.reward = null
    if (challenge.value.hashtags_list)	{
      challenge.value.hashtags_list = challenge.value.hashtags_list.replace(/[#\s]/g, '')
    }
    const res = await challengeService.createChallenge(challenge.value)
    if (res.status == 200) {
      needsValidation.value = false
      errorMessage.value = ''
      successMessage.value = "Challenge wurde erfolgreich erstellt."
      challenge.value = ''
      friends.value = ''
    }
  } catch (error) { 
    successMessage.value = ''
    errorMessage.value = ''
    if (error.response && error.response.status === 406) {
      errorMessage.value= "Diese Challenge ist nicht erlaubt."
    } else {
        errorMessage.value="Challenge erstellen hat nicht funktioniert. Bitte versuche es später erneut."
    }
  }
}

const getFriends = async () => {
  try {
    const res = await friendshipService.getFriend(store.user.id)
    if (res.status == 200) {
      friends.value = res.data
    }
  } catch (error) {
    if (error.response && error.response.status === 406) {
      alert("The challenge is illegal.")
    } else {
        alert("Error running rest-call:", error.message);
    }
  }
}

getFriends()

</script>


