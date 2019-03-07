import React from 'react';
import styled from 'styled-components';
import {connect} from 'react-redux';
import { Bar, BarFill } from './styles'
import skills from 'data/skills.json'
import education from 'data/education.json'

const HUDStyle = styled('div')`
  position: fixed;
  z-index: 2;
  left: 1em;
  top: 1em;
  color: #000;
  padding: 0.5em;
  max-width: 200px;
  border: 2px solid black;
  background: #fff;
`;


const HUD = (props) => {
  let inSchool = props.player.job.name == 'Student';

  return (
    <HUDStyle>
      {props.player.gameOver ? <div className='hud-notice'>Game Over</div> : ''}
      {inSchool ? <div className='hud-notice'>In School</div> : ''}
      <Bar><BarFill style={{width: `${props.time.monthProgress*100}%`}} /></Bar>
      <div>Time: {props.time.month}/{props.time.year}</div>
      <div>Age: {props.player.startAge + props.time.years}</div>
      <div>Cash: ${props.player.cash.toFixed(2)}</div>
      <div>Job: {props.player.job.name}</div>
      <div>Wage: ${(props.player.job.wage/12).toFixed(2)}/mo</div>
      <div>Education: {education[props.player.education].name}</div>
      {inSchool ? <div>In school for {props.player.schoolCountdown} more months</div> : ''}
      {props.player.application ? <div>Applied to {props.jobs[props.player.application.id].name}</div> : ''}
      {props.children}
    </HUDStyle>
  );
}


const mapStateToProps = (state, props) => {
  return {
    time: state.time,
    player: state.player,
    jobs: state.jobs
  };
};

export default connect(mapStateToProps)(HUD);
