import React, { useEffect } from "react";
import CardContainer from "../global/CardContainer";
import TweetForm from "../global/TweetForm";
import usePostActionContext from "../../contexts/PostActionContext";
import usePageContext from "../../contexts/pageContext";
import CommentsModal from "../global/CommentsModal";

const Home = () => {
    const { getPosts } = usePostActionContext();
    const { setData, setOnPostLike, setOnPostSave } = usePageContext();
    useEffect(() => {
        const success = (r) => {
            setData({ next: r.data.next, posts: r.data.results });
        };
        getPosts("all", success, console.log);
        return () => {
            setData({ next: null, posts: [] });
        };
    }, []);

    return (
        <div className="flex flex-col items-center w-full">
            <TweetForm />
            <CardContainer />
        </div>
    );
};

export default Home;
