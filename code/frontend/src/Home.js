import React from 'react'

import bg from './assets/bg-image2.jpg'
import sbp from './assets/search-bar-placeholder.png'
import styled from 'styled-components';
/* style from https://www.youtube.com/watch?v=f8Up35TVNgo&feature=share&ab_channel=JoeBenjamin*/
const Background = styled.div`
  background-image: url(${bg});
  background-position: left;
  background-size: cover;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100vw;
  height:100vh;
`

export const Home = () => (
    <React.Fragment>
        <Background>
        <h1>DEERCOURSE</h1>
        <br></br>
        <img src={sbp} style={{width:250}} alt="Search Bar Placeholder"/>
        </Background>
    </React.Fragment>
)