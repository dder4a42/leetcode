CC=g++
CFLAGS=-std=c++17 -Wall -Wextra -O2 -I..
TARGET=solution
SRC=solution.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(TARGET)

.PHONY: all run clean
