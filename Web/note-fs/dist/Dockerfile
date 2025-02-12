# Use the official Bun image as a base
FROM oven/bun:1.1.43

# Create and set the working directory
WORKDIR /app

# Copy the package.json and install dependencies
COPY package.json bun.lockb /app/
RUN bun install

COPY ./flag.txt /flag.flag

# Copy the rest of the application files
COPY . /app

# Expose the port the app runs on
EXPOSE 3000

# Command to run the application
CMD ["bun", "start"]
