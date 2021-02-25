import bg from '../assets/school-bg.png'
import styled from 'styled-components';

/* style from https://www.youtube.com/watch?v=f8Up35TVNgo&feature=share&ab_channel=JoeBenjamin
 * 
 * Background wraps the contents of each page
 * Background is not used as a flexbox/container
 * in order to not mess with the navbar
 */
const Background = styled.div`
  background-image: url(${bg});
  background-position: left;
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
`

/*
 * Flexbox container for all pages
 */
const Content = styled.div`
  padding: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100%;
  width: 100%;
`

const ContentCenter = styled.div`
  padding: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100%;
  width: 100%;
  flex-grow: 1;
`

export {
    Background, Content, ContentCenter
}