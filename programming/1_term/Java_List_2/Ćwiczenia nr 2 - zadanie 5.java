package com.jetbrains;
import java.util.ArrayDeque;
import java.util.PriorityQueue;

class Osoba
{
    ArrayDeque<String> ad_kolejka = new ArrayDeque<>();
    PriorityQueue<String> pq_kolejka = new PriorityQueue<>();

    public void registerMe(String name)
    {
        //gdy wstawimy kolejny element to reszta elementow pozostale nie beda juz mialy priorytetu i wroca do porzadku jak w ArrayDeque
        this.pq_kolejka.offer(name); //wstawia na poczatek jako priorytet
        this.ad_kolejka.add(name); //dodaje element na koniec kolejki
    }

    public void showQue()
    {
        System.out.println("Remaining (pq): " + pq_kolejka);
        System.out.println("Remaining (ad): " + ad_kolejka);
        System.out.println();
    }

    public void nextPls()
    {
        System.out.println(pq_kolejka.peek() + " come in please. (pq)");
        System.out.println(ad_kolejka.getFirst() + " come in please. (ad)");
        pq_kolejka.poll();
        ad_kolejka.remove();
        this.showQue();
    }
}

public class Main
{
    public static void main(String[] args)
    {
        Osoba o = new Osoba();

        o.registerMe("Konrad Konieczny");
        o.showQue();

        o.registerMe("Joe Biden");
        o.showQue();

        o.registerMe("Grzegorz Brzeczeszczykiewicz");
        o.showQue();

        o.nextPls();
        o.nextPls();
        o.nextPls();
    }
}