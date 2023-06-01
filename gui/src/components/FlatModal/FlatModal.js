import classes from './FlatModal.module.css';
import ReactDOM from 'react-dom';

const FlatModal = (props) => {
  const closeModalHandler = () => {
    console.log('close modal clicked');
    props.onClose();
  }

  return (
    <div className={classes.wrapper}>
      <p className={classes.exitButton} onClick={closeModalHandler}>X</p>
      <div className={classes.rowOne}>
        <div className={classes.image}>
          <img src={props.flat.images[0]} />
        </div>
        <div className={classes.content}>
          <h2>{props.flat.title}</h2>
          <p>{props.flat.area}</p>
          <p>{props.flat.xxx}</p>

          <div className={classes.price}>
            <h2>{props.flat.price} zł</h2>
            <p>{props.flat.pricePerMeter} zł/m2</p>
          </div>
        </div>
      </div>
      <div className={classes.rowTwo}>
        <h2>Opis</h2>
        <p>{props.flat.description}</p>
      </div>
    </div>
  );
}

const Modal = (props) => {
  return (
    <>
      {ReactDOM.createPortal(<FlatModal flat={props.flat} onClose={props.onClose} />, document.getElementById('modal-root'))}
    </>
  )
}

export default Modal;