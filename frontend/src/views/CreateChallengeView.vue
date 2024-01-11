<template>
<main>
<div class="container-md">
  <h1 class="my-4">Challenge erstellen</h1>
    <div class="col-md-5 col mt-5 m-auto">
        <form @submit.prevent="showData = true">
            <div class="mb-3">
                <label class="form-label" for="challengename">Challenge Name</label>
                <input class="form-control" id="username" type="text" v-model="formData.challengeName" placeholder="z.B. Spexen" />
            </div>
            <div class="mb-3">
              <label class="form-label" for="friendselection">Freund auswählen</label>	
                <select id="friend" class="form-select" v-model="formData.friend" aria-label="Default select example">
                  <option disabled value="">Wähle einen Freund aus</option>
                  <option value="1">1</option>
                  <option value="2">2</option>
                  <option value="3">3</option>
                </select>
            </div>
            <div class="mb-3">
                <label for="input2">Beschreibung</label>
                <input type="text" class="form-control" id="description" v-model="formData.description">
            </div>

            <div class="mb-3">
                <label for="input3">Hashtag</label>
                <input type="text" class="form-control" id="hashtags" v-model="formData.hashtags">
            </div>

            <div class="mb-3">
                <label for="input4">Reward (optional)</label>
                <input type="text" class="form-control" id="reward" v-model="formData.reward">
            </div>
            <div>
              <label for="checkbox">ChatGPT</label>
              <input type="checkbox" id="chatgpt_check" v-model="formData.chatgpt_check">
            </div>
            <button type="submit" class="btn btn-primary" @click="createChallenge()">Freund herausfordern</button>

            <div v-if="showData">{{formData}}</div>
        </form>
    </div>
</div>
</main>
</template>

<script setup>
import {ref} from 'vue'
import challengeService from "../services/challenge.service.js";
const showData = ref(false);

const formData = ref({
    challengeName: '',
    friend: '',
    description: '',
    hashtags: '',
    reward: '',
    chatgpt_check: '',
  });

const createChallenge = async () => {
  try {
    let res = {};
    res = await challengeService.createChallenge(
      formData.value.challengeName,
      formData.value.friend,
      formData.value.description,
      formData.value.hashtags,
      formData.value.reward,
      formData.value.chatgpt_check
    );
    console.log(res.data)
    alert(JSON.stringify(res.data, null, 2));
    if (res.status == 406) {
      alert("The challenge is not legal.")
    }
  } catch (error) {
    if (error.response && error.response.status === 406) {
      alert("The challenge is illegal.")
    } else {
        alert("Error running rest-call:", error.message);
    }
  }
}
</script>


