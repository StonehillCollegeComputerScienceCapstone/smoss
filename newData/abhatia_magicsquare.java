// credit: http://profajaybhatia.blogspot.com/2015/04/java-program-to-find-3x3-magic-square.html
/*
 * MagicSquare.java
 *
 * Copyright 2015 Ajay Bhatia <prof.ajaybhatia@gmail.com>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 *
 *
 */


public class MagicSquare {
    public static void main (String args[]) {
        int order = 3;
        for (int row = 0; row < order; row++) {
            for (int col = 0; col < order; col++) {
                int rowMatrix = (((order + 1) / 2 + row + col) % order);
                int colMatrix = (((order + 1) / 2 + row + order - col - 1) % order) + 1;
                System.out.print(((rowMatrix * order) + colMatrix) + "\t");
            }

            System.out.println();
        }
    }
}