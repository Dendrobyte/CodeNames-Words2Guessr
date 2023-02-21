import WordInput from "../wordinput/WordInput";
import './Grid.css'

let size: number[] = Array(25).fill(0); // Hehe

function Grid() {
    return (
        <div className="container">
            {
                size.map((_, idx) => {
                    return <span className='container-flex-item'><WordInput key={idx} /></span>
                })
            }
        </div>
    )
}

export default Grid;