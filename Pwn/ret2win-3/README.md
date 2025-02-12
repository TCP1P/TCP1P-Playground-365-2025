# ret2win 3

> Please check the [writeups](./writeups/) for adding writeups to this repository, and refer to the [solver](./solver/) if an author solver exists.

**Author:** zran

**Attachment:** [./dist/](./dist/)


## Description
Salah satu mitigasi dari buffer overflow di stack adalah canary. Canary adalah 8 byte random yang diletakkan sebelum saved RBP. Jadi, kalau kita overwrite saved RIP menggunakan buffer overflow, canary pasti akan ikut berubah. Canary akan diperiksa oleh program setiap sebelum keluar fungsi dan kalau canary-nya berubah dari sebelumnya, berarti telah terjadi buffer overflow dan program akan dihentikan. Tapi, kalau kita tau canary-nya, kita tinggal masukin ke payload kita di offset yang sesuai.

Connect: nc  19002