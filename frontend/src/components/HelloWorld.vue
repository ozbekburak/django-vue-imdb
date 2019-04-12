<template>
  <div class="main">
    <form v-on:submit.prevent="getMovie"> <!-- v-on:submit.prevent="getMovie" calls the function getMovie on submit -->
      <br>
      <h2 class="title">Get Your Movie Detail</h2>

      <div class="field">
        <label class="label">in an easy way</label>
        <div class="control">
            <input class="input is-rounded" type="text" v-model="title"> <!-- Connects this field to the title variable -->
        </div>
      </div>

      <div>
        <div class="control">
          <button class="button is-info is-rounded is-focused">Get Detail</button>
        </div>
      </div>

       <div>
        <div class="control">
          <hr>
          <span class="fa-stack">
            <i class="fas fa-camera"></i>             
          </span>
          <h1 class="subtitle"> Movie ID:  {{ moviedetail[0] }} </h1>

          <h1 class="subtitle"> Movie Title:  {{ moviedetail[1] }} </h1>

          <h1 class="subtitle"> Movie Year:  {{ moviedetail[2] }}  </h1>

          <h1 class="subtitle"> Movie Genre:  {{ moviedetail[3] }}  </h1>

          <h1 class="subtitle"> Movie Rating:  {{ moviedetail[4] }}  </h1>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  data () {
    return {
      moviedetail: '',
      title: ''
    }
  },
  methods: {
    getMovie(){
      if (this.title) {
          axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/movietitle/',
            data: {
              title: this.title
            }
         }).then((response) => {
           let newmoviedetail = response.data
           console.log(newmoviedetail)
           this.moviedetail = JSON.parse(newmoviedetail);
           
         }).catch((error) => {
           console.log(error);
         });
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.input{
  display: inline-block;
  width:50%;
  text-align: center;
}
.control{
  text-align: center;
}
</style>
