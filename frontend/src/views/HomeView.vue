<template>
  <div>
    <div class="container-md">
      <h1 class="my-4">Meine Challenges</h1>
    </div>
    <div class="container-md bg-body-secondary py-3 rounded">
      <h2 class="mb-4">Ausstehende Challenges</h2>
      <div v-if="!pendingChallenges[0]">Keine ausstehenden Challenges zurzeit!</div>
      <div v-if="pendingChallenges[0]" class="container-md bg-body-tertiary rounded py-2">
        <ul class="px-0 my-0">
          <li class="row align-items-center py-3 gy-2 gy-lg-0" v-for="pendingChallenge in pendingChallenges" :key="pendingChallenge.id">
            <div class="col-lg-2">{{pendingChallenge.title}}</div>
            <div class="col-lg-7">{{pendingChallenge.description}}</div>
            <div class="col-3 col-lg align-self-end d-flex  justify-content-lg-end d-flex-column">
              <button class="btn btn-success btn-block" @click="acceptChallenge(pendingChallenge.id)">Annehmen</button>
              <button class="btn btn-danger btn-block offset-1" @click="declineChallenge(pendingChallenge.id)">Ablehnen</button>
            </div>
          </li>
        </ul>
      </div>
    </div>

    <div class="container-md bg-body-secondary py-3 rounded mt-4">
      <h2 class="mb-4">Aktive Challenges</h2>
      <div v-if="!acceptedChallenges[0]">Keine aktiven Challenges zurzeit!</div>
      <div  v-if="acceptedChallenges[0]" class="container-md bg-body-tertiary rounded py-2">
        <ul class="px-0 my-0">
          <li  class="row align-items-center py-3 gy-2 gy-lg-0" v-for="acceptedChallenge in acceptedChallenges" :key="acceptedChallenge.id">
            <div class="col-lg-2">{{acceptChallenge.title}}</div>
            <div class="col-lg-7">{{acceptChallenge.description}}</div>
            <div class="col-3 col-lg align-self-end d-flex  justify-content-lg-end d-flex-column">
              <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#proveModal">Abschließen</button>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>

      <div class="modal fade" id="proveModal" tabindex="-1" aria-labelledby="challengeFinishLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h2 class="modal-title h5" id="challengeFinishLabel">Challenge abschließen</h2>
                    <button class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form>
                      <div class="mb-3">
                        <label for="formFile" class="form-label">Foto oder Video hochladen</label>
                        <input class="form-control" id="formFile" type="file" name="image" accept="image/png, image/jpg, image/jpeg, video/mp4" capture="user">
                      </div>
                      <button class="btn btn-primary">Senden</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import challengeService from "../services/challenge.service";
import {useStore} from '../stores/store'
import {ref} from 'vue'

const store = useStore()
const pendingChallenges = ref([])
const acceptedChallenges = ref([])
console.log(acceptedChallenges.value)

const getAcceptedChallenges = async () => {
  try {
    const res = await challengeService.getAcceptedChallenges(store.user.id)
    if (res.status == 200) {
      acceptedChallenges.value = res.data
      console.log(acceptedChallenges.value)
    }
  } catch (error) {
    console.log(error)
  }
}

const getPendingChallenges = async () => {
  try {
    const res = await challengeService.getPendingChallenges(store.user.id)
    if (res.status == 200) {
      pendingChallenges.value = res.data
      console.log(pendingChallenges.value)
    }
  } catch (error) {
    console.log(error)
  }
}

getAcceptedChallenges()
getPendingChallenges()
</script>