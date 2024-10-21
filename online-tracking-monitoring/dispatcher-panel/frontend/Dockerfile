# Use Node.js image
FROM node:14-alpine

# Set work directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Copy project files
COPY . .

# Expose port
EXPOSE 3000

# Start the app
CMD ["npm", "start"]
