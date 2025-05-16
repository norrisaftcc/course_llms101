-- Supabase SQL Schema for AI Blog Application
-- Run this in your Supabase SQL editor

-- Create posts table
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    topic TEXT,
    tone VARCHAR(50),
    meta_description VARCHAR(160),
    meta_keywords TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create index for faster queries
CREATE INDEX idx_posts_created_at ON posts(created_at DESC);

-- Enable Row Level Security
ALTER TABLE posts ENABLE ROW LEVEL SECURITY;

-- Create policy for public read access
CREATE POLICY "Posts are viewable by everyone" ON posts
    FOR SELECT USING (true);

-- Create policy for authenticated write access (optional)
CREATE POLICY "Authenticated users can create posts" ON posts
    FOR INSERT WITH CHECK (auth.role() = 'authenticated');

-- Create a function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create trigger for automatic timestamp updates
CREATE TRIGGER update_posts_updated_at BEFORE UPDATE
    ON posts FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Create comments table (for future enhancement)
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES posts(id) ON DELETE CASCADE,
    author_name VARCHAR(100),
    content TEXT NOT NULL,
    is_approved BOOLEAN DEFAULT false,
    sentiment_score FLOAT, -- For AI moderation
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create index for comments
CREATE INDEX idx_comments_post_id ON comments(post_id);

-- Sample data (optional)
INSERT INTO posts (title, content, topic, tone, meta_description, meta_keywords)
VALUES 
    ('Welcome to AI Blogging', 
     'This is your first AI-powered blog post. The possibilities are endless!', 
     'Introduction to AI blogging',
     'Professional',
     'Discover the power of AI-generated content for your blog',
     'AI, blogging, content generation, automation'),
    ('The Future of Content Creation', 
     'AI is revolutionizing how we create and consume content. Here''s what you need to know...', 
     'AI and content creation',
     'Conversational',
     'Explore how AI is transforming content creation',
     'AI, content creation, future, technology, writing');