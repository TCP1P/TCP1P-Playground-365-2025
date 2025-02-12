# ret2win 4

> Please check the [writeups](./writeups/) for adding writeups to this repository, and refer to the [solver](./solver/) if an author solver exists.

**Author:** zran

**Attachment:** [./dist/](./dist/)


## Description
Mitigasi lain untuk menyusahkan penyerang dalam mengubah alur program adalah PIE. PIE adalah singkatan dari Position Independent Executable yang mengakibatkan program kita untuk di-load ke dalam memori dengan offset random. Jadi walaupun ada buffer overflow, penyerang tidak tau alamat dari fungsi/instruksi yang ingin dijalankan. Tapi, kalau kita bisa dapetin salah satu alamat dari program saat dijalankan, alamat dari fungsi/instruksi yang ingin dijalankan tinggal dihitung dari selisihnya dengan alamat yang udah didapetin tadi.

Connect: nc  19003