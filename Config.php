<?php

/**
 * Created by PhpStorm.
 * User: root
 * Date: 7/19/17
 * Time: 8:48 AM
 */
class Config
{
    private $ssh_host = NULL;
    private $ssh_port = NULL;
    private $ssh_username = NULL;

    public function __construct($ssh_host,$ssh_port,$ssh_username)
    {
        if(empty($ssh_host) || empty($ssh_port) || empty($ssh_username))
        {
            throw new InvalidArgumentException('Config::__construct() missing required parameters');
        }

        $this->ssh_port = $ssh_port;
        $this->ssh_host = $ssh_host;
        $this->ssh_username = $ssh_username;
    }

    public function ssh_getHost()
    {
        return $this->ssh_host;
    }

    public function ssh_getUsername()
    {
        return $this->ssh_username;
    }

    public function ssh_getPort()
    {
        return $this->ssh_port;
    }

}