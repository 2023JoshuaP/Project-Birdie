import React from "react";
import usePageContext from "../../contexts/pageContext";
import Card from "./Card";
import PropTypes from "prop-types";

const CardContainer = (props) => {
    const {
        data: { posts },
    } = usePageContext();
    let results = posts;
    if (props.posts) results = props.posts;
    const { onLike, onSave, onComment } = props;

    return (
        <>
            {results.map((post) => {
                return (
                    <Card
                        id={post.id}
                        // Trying to randomize the key has much has possible to prevent conflict
                        // when dealing with newly requested posts from paginization
                        key={post.id + new Date().toJSON() + Math.random() ** Math.random()}
                        user={post.creator.username}
                        card_content={post.content}
                        card_image={post.image}
                        onLike={onLike}
                        onComment={onComment}
                        onSave={onSave}
                        comments={post.comments}
                        likes={post.likes}
                        saves={post.saves}
                        liked={post.is_liked}
                        avatar={post.creator.profile_pic}
                        creator_id={post.creator.id}
                        is_saved={post.is_saved}
                        is_commented={post.is_commented}
                        is_following_user={post.is_following_user}
                        is_followed_by_user={post.is_followed_by_user}
                        created={post.created}
                        isEdited={post.isEdited}
                    />
                );
            })}
        </>
    );
};

CardContainer.propTypes = {
    posts: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
            creator: PropTypes.shape({
                username: PropTypes.string.isRequired,
                profile_pic: PropTypes.string.isRequired,
                id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
            }).isRequired,
            content: PropTypes.string.isRequired,
            image: PropTypes.string,
            comments: PropTypes.array,
            likes: PropTypes.number,
            saves: PropTypes.number,
            is_liked: PropTypes.bool,
            is_saved: PropTypes.bool,
            is_commented: PropTypes.bool,
            is_following_user: PropTypes.bool,
            is_followed_by_user: PropTypes.bool,
            created: PropTypes.string,
            isEdited: PropTypes.bool,
        })
    ),
    onLike: PropTypes.func,
    onSave: PropTypes.func,
    onComment: PropTypes.func,
};

export default CardContainer;