import './App.css';
import React from 'react';
const genre="Horror";
const Stats = ({showsWatched, watchTime})=>{
  return(
    <div className="flex flex-row px-10 mr-10">
        <div className="bg-transparent border border-1 border-gray-400 h-[100px] w-[100px] flex justify-center items-center flex-col">
          <p className="text-3xl font-bold text-red-400">{showsWatched}</p>
          <p className="text-xs font-light opacity-45 text-center rounded-tl-sm rounded-bl-sm">Shows watched</p>
        </div>
        <div className="bg-transparent border border-1 border-gray-400 h-[100px] w-[100px] flex justify-center items-center flex-col">
          <p className="text-3xl font-bold text-red-400">{watchTime}<span className="text-xs font-light opacity-45 ">hr</span></p>
          <p className="text-xs font-light opacity-45 text-center">Watch-Time</p>
        </div>
        <div className="bg-transparent border border-1 border-gray-400 h-[100px] w-[100px] flex justify-center items-center flex-col rounded-tr-sm rounded-br-sm">
          <p className="text-3xl font-bold text-red-400">5</p>
          <p className="text-xs font-light opacity-45 text-center">devices</p>
        </div>
      </div>
  );
}
const Profile=({name, joinedDay, joinedMonth, joinedYear})=>{
  return(
    <div className="flex gap-10 mb-5 p-3 sm:pl-10 ">
      <div className="h-[100px] w-[100px] bg-red-500 m-1"></div>
      <div className="text-white ">
          <p className="text-3xl font-bold mb-1">{name}</p>
          <p className="text-md font-light opacity-45">Joined on {joinedDay} {joinedMonth} {joinedYear}</p>
        </div>
    </div>
  );
}
const NavBar=()=>{
  return(
    <div className="w-screen h-[50px] bg-test mb-5">NavBar</div>
  );
}
function User() {
  return (
    <div className="min-h-screen w-screen bg-gblack  flex justify-center items-center newfont flex-col inset-5 text-white">
      <NavBar/>

      <div className="flex flex-col sm:flex-row relative bg-trx w-full items-center mb-10 sm:place-content-around">
        <Profile name="Saul" joinedDay="5" joinedMonth="August" joinedYear="2022" className=""/>
        <Stats watchTime={10} showsWatched={97} className=""/>
      </div>

      {/* //genre taste */}
      <div className="flex flex-row items-center justify-center m-3 mb-10 lg:p-5 w-full h=full bg-tran">
        <div className="rounded-full bg-red-500 flex items-center h-[150px] md:h-[200px] md:w-[200px] w-[150px]  m-4"></div>
        <div className="text-white ">
          <p className="text-4xl m-2">You love <span className="font-bold">{genre}</span>, don't you?</p>
        </div>
      </div>
      {/* Our picks */}
      <div className="m-3 grid w-full h-full grid-rows-1 md:grid-cols-6 lg:grid-cols-10 gap-2 bg-tran">
        <p className="row-start-1 col-start-2 col-end-10 text-2xl font-semibold m-5">Our best picks for you..</p>
      </div>
      <div className="h-[300px] w-full bg-test text-center flex justify-center items-center">Carousel here</div>
      <div className="flex h-[100px]"></div>
    </div>
  );
}

export default User;