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
        <br>
        <button class="button is-info is-rounded is-focused">Get Detail</button>
        <hr>
      </div> 
      
      <table is-fullwidth align="right" class="table" >
        <thead>
            <tr>
              <th>Locations</th>
            </tr>        
        </thead>            
        <tbody>
          <tr v-for="index in locationList.length">                
            <td>{{ locationList[index-1] }}</td>          
          </tr>
        </tbody>                  
      </table>

        <table is-fullwidth align="left" class="table">
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
          <tr v-for="index in (songList.length)">                
             <td>{{ songList[index-1] }}</td>
             <td>{{ writerList[index-1] }}</td>
             <td>{{ performerList[index-1] }}</td>                
          </tr>
         </tbody>                  
       </table> 
      
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'MainPage',
  data () {
  
    return {
      moviedetail: '',
      title: '',
      locationList: [],
      songList: [],
      writerList: [],
      performerList: []      
    }
  },
  methods: {
    getMovie(){
      if (this.title) {
          axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/moviedetail/',
            data: {
              title: this.title
            }
         }).then((response) => {
           let newmoviedetail = response.data;            
           this.moviedetail = JSON.parse(newmoviedetail);         
           let i;
           
           

           // önceki aramayla append olmaması için location listesini boşaltıyoruz.
           this.locationList = []
           for(i = 0; i<this.moviedetail[6].length; i++){
            this.locationList.push(this.moviedetail[6][i])
           }
           console.log(this.locationList)

           
           // şarkı listesi için uzunluk alıyoruz.
           let songsLength = Object.keys(this.moviedetail[5]).length;           

           // önceki aramayla birbirlerine append olmaması için listeyi boşaltıyoruz.
           this.songList = []
           for(i=0; i < songsLength; i++ ){             
             this.songList.push(Object.entries(this.moviedetail[5][i])[0][0])
             this.writerList.push(Object.entries(this.moviedetail[5][i])[0][1]['written by'])
             this.performerList.push(Object.entries(this.moviedetail[5][i])[0][1]['performed by'])             
           }
        
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
