package com.jetbrains;

class Program
{
    private String name;
    private String license;
    private double version;
    private short contributors_count;
    private int commits;
    private boolean crossplatform;
    private boolean opensource;
    private char out_of_date;

    public Program()
    {
        this("Noname", "Unknown", 0.0, (short) 0, 0, false, false, 'y');
    }

    public Program(String n, String l, double v, short c_c, int c, boolean cp, boolean os, char o_f_d)
    {
        this.name = n;
        this.license = l;
        this.version = v;
        this.contributors_count = c_c;
        this.commits = c;
        this.crossplatform = cp;
        this.opensource = os;
        this.out_of_date = o_f_d;
    }

    public Program(String error)
    {
        this.name = error;
        this.license = error;
        this.version = -1.1;
        this.contributors_count = -1;
        this.commits = -1;
        this.out_of_date = 'e';
    }

    public void setLicense(String l)
    {
        this.license = l;
    }

    public void setName(String n)
    {
        this.name = n;
    }

    public void setVersion(double v)
    {
        this.version = v;
    }

    public void setContributors_count(short c_c)
    {
        this.contributors_count = c_c;
    }

    public void setCommits(int c)
    {
        this.commits = c;
    }

    public void setCrossplatform(boolean cp)
    {
        this.crossplatform = cp;
    }

    public void setOpensource(boolean os)
    {
        this.opensource = os;
    }

    public void setOut_of_date(char o_f_d)
    {
        this.out_of_date = o_f_d;
    }

    public String getLicense()
    {
        return license;
    }

    public String getName()
    {
        return name;
    }

    public double getVersion()
    {
        return version;
    }

    public short getContributors_count()
    {
        return contributors_count;
    }

    public int getCommits()
    {
        return commits;
    }

    public boolean isCrossplatform()
    {
        return crossplatform;
    }

    public boolean isOpensource()
    {
        return opensource;
    }

    public char getOut_of_date()
    {
        return out_of_date;
    }

    public void printMe()
    {
        System.out.print("Name: " + getName() + " | License: " + getLicense() + " | Version: " + getVersion() +
                " | Contributors count: " + getContributors_count() + " | Commits: " + getCommits()
                + " | Crossplatform: " + isCrossplatform() + " | Opensource: " + isOpensource() +
                " | Out of date?: " + getOut_of_date() + "\n");
    }
}

public class lista3_zad8
{
    public static void main(String[] args)
    {
        Program empty = new Program();
        empty.printMe();

        Program windows_terminal = new Program();

        windows_terminal.setName("Windows Terminal");
        windows_terminal.setLicense("MIT");
        windows_terminal.setVersion(1.11);
        windows_terminal.setContributors_count((short) 309);
        windows_terminal.setCommits(2744);
        windows_terminal.setCrossplatform(false);
        windows_terminal.setOpensource(true);
        windows_terminal.setOut_of_date('n');

        windows_terminal.printMe();

        Program linux_kernel = new Program("Linux kernel", "GPLv2", 5.16, (short) 5000, 1070782, false, true, 'n');
        linux_kernel.printMe();

        Program vim = new Program("Vim", "Vim", 8.2, (short) 84, 15181, true, true, 'n');
        vim.printMe();

        Program error = new Program("Error");
        error.printMe();

        Program fixed_mpv = new Program("Error");

        fixed_mpv.setName("mpv");
        fixed_mpv.setLicense("GPLv2");
        fixed_mpv.setVersion(0.34);
        fixed_mpv.setContributors_count((short) 352);
        fixed_mpv.setCommits(49391);
        fixed_mpv.setCrossplatform(true);
        fixed_mpv.setOpensource(true);
        fixed_mpv.setOut_of_date('n');

        fixed_mpv.printMe();
    }
}