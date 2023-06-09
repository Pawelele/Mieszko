import classes from './FlatModal.module.css';
import ReactDOM from 'react-dom';

const FlatModal = (props) => {
  const closeModalHandler = () => {
    console.log('close modal clicked');
    props.onClose();
  }

  return (
    <div className={classes.wrapper}>
      <p className={classes.exitButton} onClick={closeModalHandler}>x</p>
      <div className={classes.rowOne}>
        <div className={classes.image}>
          <img src={props.flat.photo} />
        </div>
        <div className={classes.content}>
          <h3 className={classes.title}>{props.flat.title}</h3>
          <p>{props.flat.area}</p>
          <p>{props.flat.rooms} pokoje</p>
          <p>{props.flat.type}</p>

          <div className={classes.price}>
            <h2>{props.flat.price}</h2>
            <p>{props.flat.price_per_meter}</p>
          </div>
        </div>
      </div>
      <div className={classes.rowTwo}>
        <h3>Opis</h3>
        <p>{props.flat.description}</p>
        <a href={props.flat.link} target="_blank"><button className={classes.button}>Zobacz ofertę</button></a>
      </div>
    </div>
  );
}

const Backdrop = (props) => {
  return (
    <div className={classes.backdrop} onClick={props.onClose}></div>
  )
}

const Modal = (props) => {
  return (
    <>
      {ReactDOM.createPortal(<FlatModal flat={props.flat} onClose={props.onClose} />, document.getElementById('modal-root'))}
      {ReactDOM.createPortal(<Backdrop onClose={props.onClose} />, document.getElementById('backdrop-root'))}
    </>
  )
}

export default Modal;