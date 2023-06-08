import React, { useEffect } from "react";
import { discover } from "../../../dummyData"
import Heading from "../../common/heading/Heading"
import "./style.css"



const Discover = () => {
  const Discover = () => {
    useEffect(() => {
      fetch('http://127.0.0.1:8000/')
        .then(res => {
          if (!res.ok) {
            throw new Error("Network response was not ok");
          }
          return res.json();
        })
        .then(data => console.log(data))
        .catch(error => console.log("Fetch error:", error));
    }, []);}
  
  return (
    <>
      <section className='discover'>
        <div className='container'>
          <Heading title='Discover' />
          <div className='content'>
            {discover.map((val) => {
              return (
                <div className='box'>
                  <div className='img'>
                    <img src={val.cover} alt='' />
                  </div>
                  <h1 className='title'>{val.title}</h1>
                </div>
              )
            })}
          </div>
        </div>
      </section>
    </>
  )
}

export default Discover