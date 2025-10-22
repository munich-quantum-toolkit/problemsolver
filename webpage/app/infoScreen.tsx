import styles from './style.module.css'

const InfoScreen: React.FC = () => {
    return (
        <div className={styles.canvas + " " + styles.infoCanvas}>
            <h1>MQT QUBOMaker: Pathfinder</h1>
            <p>This web app is a supporting GUI for the MQT QUBOMaker framework. It allows users to define pathfinding problems using a set of constraints that can be converted into a QUBO formulation by the framework.</p>
            <p>Further details are given in the following paper: D. Rovara, N. Quetschlich, and R. Wille <a href="https://arxiv.org/abs/2404.10820">&quot;A Framework to Formulate Pathfinding Problems for Quantum Computing&quot;</a>, arXiv, 2024</p>
            <p>The corresponding code can be found in the framework&apos;s <a href="https://github.com/cda-tum/mqt-qubomaker">GitHub repository</a>.</p>
            <p>MQT QUBOMaker is part of the <a href="https://mqt.readthedocs.io/">Munich Quantum Toolkit</a> (MQT) developed by the <a href="https://www.cda.cit.tum.de/">Chair for Design Automation</a> at the <a href="https://www.tum.de/">Technical University of Munich</a>.</p>
        </div>
    );
}

export default InfoScreen;