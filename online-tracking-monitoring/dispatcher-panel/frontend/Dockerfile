



FROM node:16

WORKDIR /usr/src/app

COPY package.json ./
RUN npm install

COPY . .

CMD ["npm", "start"]





# Use Node.js base image
FROM node:16-alpine

# Set work directory
WORKDIR /app

# Copy the package.json and install dependencies
COPY package.json /app/
RUN npm install

# Copy the rest of the project files
COPY . /app/

# Build the app for production
RUN npm run build

# Expose port 3000 for the frontend
EXPOSE 3000

# Serve the app using a lightweight web server
CMD ["npx", "serve", "-s", "build", "-l", "3000"]
