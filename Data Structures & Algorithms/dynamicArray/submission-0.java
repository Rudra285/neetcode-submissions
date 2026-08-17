class DynamicArray {
    public int array[];
    public int size;
    private int capacity;

    public DynamicArray(int capacity) {
        this.size = 0;
        this.capacity = capacity;
        this.array = new int[capacity];
    }

    public int get(int i) {
        return(this.array[i]);
    }

    public void set(int i, int n) {
        this.array[i] = n;
    }

    public void pushback(int n) {
        if(this.size == this.capacity) {
            this.resize();
        }
        this.array[this.size++] = n;
    }

    public int popback() {
        this.size--;
        return(this.array[this.size]);
    }

    private void resize() {
        this.capacity*=2;
        int newArr[] = new int[this.capacity];
        for (int i = 0; i < this.size; i++) {
            newArr[i] = this.array[i];
        }
        this.array = newArr;
    }

    public int getSize() {
        return(this.size);
    }

    public int getCapacity() {
        return(this.capacity);
    }
}
