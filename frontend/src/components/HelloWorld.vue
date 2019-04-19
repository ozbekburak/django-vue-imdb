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
                  
        <table align="center" class="table">
            <thead>
              <tr>
                <th>Movie ID</th>
                <th>Title</th>
                <th>Year</th>
                <th>Genre</th>
                <th>Rating</th>
              </tr>        
            </thead>
            
            <tbody>
              <tr>
                <td>{{ moviedetail[0] }}</td>
                <td>{{ moviedetail[1] }}</td>
                <td>{{ moviedetail[2] }}</td>
                <td>{{ moviedetail[3] }}</td>
                <td>{{ moviedetail[4] }}</td>
              </tr>
            </tbody>                  
          </table>


          <table align="center" class="table">
            <thead>
              <tr>
                <th>Song Name</th>
                <th>Written By</th>
                <th>Performed By</th>
              </tr>        
            </thead>
            
            <tbody>
              <tr>
                <td>{{ songName }}</td>
                <td>{{ writer }}</td>
                <td>{{ performer }}</td>
              </tr>
            </tbody>                  
          </table>

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
      title: '',
      movieSoundtrack: '',
      songName: '',
      writer: '',
      performer: ''      
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
           this.moviedetail = JSON.parse(newmoviedetail);
           
           this.songName = Object.entries(this.moviedetail[5][3])[0][0]
           this.writer = Object.entries(this.moviedetail[5][3])[0][1]['written by']
           this.performer = Object.entries(this.moviedetail[5][3])[0][1]['performed by']

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

th{
  text-align: center;
}
</style>
